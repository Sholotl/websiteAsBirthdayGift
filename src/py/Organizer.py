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


def removePop(ID=None):
    format("RemovePop")
    locations = loadLocation()
    content = loadContent()

    if ID is None:
        ID = max(x["id"] for x in locations)

    locations = [x for x in locations if x["id"] != ID]
    content = [x for x in content if x["id"] != ID]

    save(locationsPath, sortLocations(locations))
    save(contentPath, sortContent(content))

""" -------------------------------Useless def - just format-------------------------------"""

def format(texto, length = 80, bar_length = 70):
    print(("_" * bar_length).center(length))
    print(texto.center(length))
    print(("¯" * bar_length).center(length))

"""--------------------------"""

def newData():
    format("Content")
    day, month, year = input("Enter the date (dd/mm/yyyy): ").split("/")
    date = [int(day), int(month), int(year)]
    title = input("Enter the title: ")
    note = input("Enter the note: ")
    photo = input("Enter the photo path: ")
    audio = input("Enter the audio path: ") or None
    hide = input("Hide (True/False): ").strip().lower() == "true"

    format("Locations")
    lat, lng = input("Enter the latitude and longitude (lat, lng): ").split(",")

    newContent = {
        "date": date,
        "title": title,
        "note": note,
        "photo": photo,
        "audio": audio,
        "hide": hide
    }

    newLocation = {
        "lat": float(lat.strip()),
        "lng": float(lng.strip()),
        "date": date
    }

    addPop(newContent, newLocation)


if __name__ == "__main__":
    format("UwU")
    print("1 - add pop \n2 - remove pop")
    

    match input("Option: "):
        case "1": newData()
        case "2": 
            if Id:=input("ID: "):
                removePop(Id)
            else: removePop()










