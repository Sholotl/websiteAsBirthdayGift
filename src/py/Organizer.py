import json
from datetime import datetime

"""
This code is not designed to work with an empty JSON. It is purely administrative 
and intended to assist in creating pop-ups on the map. It is not meant to operate 
outside of its intended use cases.

"""

locationsPath = './src/data/locations.json'
contentPath = './src/data/content.json'

#===================================================================
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

#===================================================================

def sortLocations(locations):
    return sorted(locations, key=lambda x: datetime(x["date"][2], x["date"][1], x["date"][0]))

def sortContent(content):
    return sorted(content, key=lambda x: datetime(x["date"][2], x["date"][1], x["date"][0]))

#===================================================================

def addPop(content, locations, newContent, newLocation):

    locations.append(newLocation)
    content.append(newContent)

    save(locationsPath, sortLocations(locations))
    save(contentPath, sortContent(content))

#===================================================================

def removePop():

    locations = loadLocation()
    content = loadContent()
    id = max(x["id"] for x in locations) 
    #-----------------------------------------------------
    format("RemovePop")
    print(f"Last enter id: {id}")
    
    IdRemoved = input("Enter the ID to remove: ")
    if not IdRemoved: IdRemoved = id

    locations = [x for x in locations if x["id"] != (IdRemoved:=int(IdRemoved))]
    content = [x for x in content if x["id"] != IdRemoved]

    save(locationsPath, sortLocations(locations))
    save(contentPath, sortContent(content))
    format("Pop removed")

#===================================================================
#So uselees fañlskdj, just format
def format(texto, length = 80, bar_length = 70):
    """Useless for the logic, just format"""
    print(("_" * bar_length).center(length))
    print(texto.center(length))
    print(("¯" * bar_length).center(length))

#===================================================================

def newData():

    locations = loadLocation()
    content = loadContent()
    id = max(x["id"] for x in locations) 
    #-----------------------------------------------------
    format("Content")
    print(f"Last enter id: {id}")

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
        "id": id + 1,
        "date": date,
        "title": title,
        "note": note,
        "photo": photo,
        "audio": audio,
        "hide": hide
    }

    newLocation = {
        "id": id + 1,
        "lat": float(lat.strip()),
        "lng": float(lng.strip()),
        "date": date
    }

    addPop(content, locations, newContent, newLocation)
    format("Added to the JSON")

if __name__ == "__main__":
    while True:
        format("UwU")
        print("1 - add pop \n2 - remove pop")
        match input("Option: "):
            case "1": newData()
            case "2": removePop()










