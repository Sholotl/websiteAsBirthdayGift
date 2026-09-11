import json

locationsPath = "../data/locations.json"
contentPath = "../data/content.json"

def loadLocation():
    with open(locationsPath) as file:
        data = json.load(file)
        return data

def loadContent():
    with open(contentPath) as file:
        data = json.load(file)
        return data


def save(path, newData):
    with open(path, "w") as file:
        json.dump(newData, file, indent=2, ensure_ascii=False)






