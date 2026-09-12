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


newC = {
    "date": [
      2,
      2,
      2026
    ],
    "title": "Cuando Yolo jugaba roblox...",
    "note": "Cuando empezábamos a juegar yo no tenia idea de muchos juegos y me ENCANTA roblox, entonces era lo único que jugábamos, debo decir que también eran muy buenos tiempos ahora Yolo ya dice que no y hemos probado mas juegos también muy interesantes, probablemente de las mejores cosas que le paso a la relación, es muy divertido y gracioso jugar juntos, se siente como algo muy cercano que ahora forma parte de mi dia a dia, gracias ROBLOX y Yolo, los amo MUCHO a ambos. ",
    "photo": "src/assets/photos/020226.png",
    "audio": None,
    "hide": False
    }

newL = {
    "lat": 19.0726359,
    "lng": -98.2222316,
    "date": [
      2,
      2,
      2026
    ]
    }

addPop(newC, newL)


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




