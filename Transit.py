import googlemaps
import requests
import ujson as json


def getKey():
    file = open("TransitAPI.txt","r")
    key = file.readline()
    file.close()
    return key

#the mctc adress
mctcAdress = "mctc+minneapolis"
#getting the api key
apiKey = getKey()

#asking the user if they are traveling from or to MCTC
travel = input(str("From or to MCTC: "))
if travel == "to":
    #asking for the current adress and formating to fit in URL
    currentAdress = input(str("Enter current adress: "))
    currentAdress = currentAdress.replace(" ","+")
    formatedURL = "https://maps.googleapis.com/maps/api/" \
          "directions/json?origin={0}&destination={1}&mode=transit&key={2}".format(currentAdress,mctcAdress,apiKey)

    request = requests.get(formatedURL)
    print(request)
    json_data = json.loads(request.content)
    #printing necessary data
    instructions = json_data["routes"][0]["legs"][0]["steps"][0]["html_instructions"]
    bus = json_data["routes"][0]["legs"][0]["steps"][1]["transit_details"]["headsign"]
    departureTime = json_data["routes"][0]["legs"][0]["steps"][1]["transit_details"]["departure_time"]["text"]
    arrivalTime = json_data["routes"][0]["legs"][0]["steps"][1]["transit_details"]["arrival_time"]["text"]
    busTravelTime = json_data["routes"][0]["legs"][0]["steps"][1]["duration"]["text"]
    route = json_data["routes"][0]["legs"][0]["steps"][1]["transit_details"]["line"]["url"]

    print("Instructions: " + instructions +"\nBus: "+ bus + "\nDeparture time: " + departureTime+"\nArrival time: " + arrivalTime
          +"\nBus travel time: " + busTravelTime + "\nRoute: " + route)

elif travel == "from":
    #asking user for destination adress
    currentAdress = input(str("Enter destination adress: "))
    currentAdress = currentAdress.replace(" ", "+")
    formatedURL = "https://maps.googleapis.com/maps/api/" \
                  "directions/json?origin={0}&destination={1}&mode=transit&key={2}".format(mctcAdress, currentAdress,
                                                                                           apiKey)
    request = requests.get(formatedURL)
    print(request)
    json_data = json.loads(request.content)
    instructions = json_data["routes"][0]["legs"][0]["steps"][0]["html_instructions"]
    bus = json_data["routes"][0]["legs"][0]["steps"][1]["transit_details"]["headsign"]
    departureTime = json_data["routes"][0]["legs"][0]["steps"][1]["transit_details"]["departure_time"]["text"]
    arrivalTime = json_data["routes"][0]["legs"][0]["steps"][1]["transit_details"]["arrival_time"]["text"]
    busTravelTime = json_data["routes"][0]["legs"][0]["steps"][1]["duration"]["text"]
    route = json_data["routes"][0]["legs"][0]["steps"][1]["transit_details"]["line"]["url"]

    print(
        "Instructions: " + instructions + "\nBus: " + bus + "\nDeparture time: " + departureTime + "\nArrival time: " + arrivalTime
        + "\nBus travel time: " + busTravelTime + "\nRoute: " + route)






