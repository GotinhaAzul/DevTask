from pathlib import Path

from fastapi.testclient import TestClient

from mycode.api import app, get_user_manager
from mycode.helpers import setup
from mycode.user_storage import User_Storage
from mycode.usermanager import UserManager


def _client_with_temp_db(file="testregister.db"):
    setup(file)
    storage = User_Storage(database=file)
    manager = UserManager(storage=storage)
    app.dependency_overrides[get_user_manager] = lambda: manager
    client = TestClient(app)
    return client, storage


def _teardown(file="testregister.db", storage=None):
    app.dependency_overrides.clear()
    if storage is not None:
        storage.close()
    Path(file).unlink(missing_ok=True)


def test_register_success():
    file = "testregister.db"
    client, storage = _client_with_temp_db(file)
    try:
        response = client.post("/register", params={"user_id": 1}, json={"username": "alice", "password": "secret"})
        assert response.status_code == 201
        body = response.json()
        assert body["username"] == "alice"
        assert body["id"] == 1
        assert "password" not in body
    finally:
        _teardown(file, storage)


def test_register_duplicate_username_returns_409():
    file = "testregister.db"
    client, storage = _client_with_temp_db(file)
    try:
        r1 = client.post("/register", params={"user_id": 1}, json={"username": "bob", "password": "secret"})
        assert r1.status_code == 201

        r2 = client.post("/register", params={"user_id": 2}, json={"username": "bob", "password": "other"})
        assert r2.status_code == 409
        assert "detail" in r2.json()
    finally:
        _teardown(file, storage)


def test_register_invalid_username_returns_422():
    file = "testregister.db"
    client, storage = _client_with_temp_db(file)
    try:
        response = client.post("/register", params={"user_id": 1}, json={"username": "   ", "password": "secret"})
        assert response.status_code == 422
    finally:
        _teardown(file, storage)


def test_register_duplicate_userid_returns_409():
    file = "testregister.db"
    client, storage = _client_with_temp_db(file)
    try:
        r1 = client.post("/register", params={"user_id": 5}, json={"username": "carol", "password": "secret"})
        assert r1.status_code == 201

        r2 = client.post("/register", params={"user_id": 5}, json={"username": "dave", "password": "secret"})
        assert r2.status_code == 409
    finally:
        _teardown(file, storage)
