import json
from datetime import datetime

locationsPath = './src/data/locations.json'
contentPath = './src/data/content.json'

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

def sortLocations(locations):
    return sorted(locations, key=lambda x: datetime(x["date"][2], x["date"][1], x["date"][0]))

def sortContent(content):
    return sorted(content, key=lambda x: datetime(x["date"][2], x["date"][1], x["date"][0]))

def addPop(newContent, newLocation):
    locations = loadLocation()
    content = loadContent()
    newID = max([x["id"] for x in locations], default=0) + 1

    #-----
    newLocation = {"id": newID, **newLocation}
    newContent = {"id": newID, **newContent}
    #-----

    locations.append(newLocation)
    content.append(newContent)

    save(locationsPath, sortLocations(locations))
    save(contentPath, sortContent(content))

"""
newC = {
    "date": [
      11,
      9,
      2026
    ],
    "title": "holi chami",
    "note": "Desde la Mac de chame",
    "photo": "src/assets/photos/051225.jpg",
    "audio": None,
    "hide": False
    }

newL = {
    "lat": 20.1172903,
    "lng": -100.3055894,
    "date": [
      11,
      9,
      2026
    ]
    }

addPop(newC, newL)
"""

"""x
def removePop():
    locations = loadLocation()
    content = loadContent()

    if len(locations) > 0:
        locations.pop()
        content.pop()

    save(locationsPath, sortLocations(locations))
    save

"""




