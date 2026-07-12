import json

class Storage:
    def write(self, content, filename):
        with open(filename, "r") as f:
            data = json.load(f)

        data["tasks"].append(content)

        with open(filename, "w") as f:
            json.dump(data, f, indent=4)

    def save(self, content, filename):
        with open(filename, "w") as f:
            json.dump(content, f, indent=4)

    def read(self, filename) -> dict:
        with open(filename, "r") as f:
            data = json.load(f)
        return data
