from mycode.main import create, delete, check

def test_create():
    create("Teste", 9999)
    assert check(9999) == True
    delete(9999)
