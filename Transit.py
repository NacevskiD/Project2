import googlemaps
import requests
import ujson as json


def getKey():
    file = open("TransitAPI.txt","r")
    key = file.readline()
    file.close()
    return key

class Transit:
    def __init__(self):
        #the mctc adress
        self.mctcAdress = "mctc+minneapolis"
        #getting the api key
        self.apiKey = getKey()

    #asking the user if they are traveling from or to MCTC
    def getRouteTo(self,adress):

        #asking for the current adress and formating to fit in URL
        formatedURL = "https://maps.googleapis.com/maps/api/" \
                  "directions/json?origin={0}&destination={1}&mode=transit&key={2}".format(adress,self.mctcAdress,self.apiKey)

        request = requests.get(formatedURL)
        json_data = json.loads(request.content)
        #printing necessary data
        instructions = json_data["routes"][0]["legs"][0]["steps"][0]["html_instructions"]
        bus = json_data["routes"][0]["legs"][0]["steps"][1]["transit_details"]["headsign"]
        departureTime = json_data["routes"][0]["legs"][0]["steps"][1]["transit_details"]["departure_time"]["text"]
        arrivalTime = json_data["routes"][0]["legs"][0]["steps"][1]["transit_details"]["arrival_time"]["text"]
        busTravelTime = json_data["routes"][0]["legs"][0]["steps"][1]["duration"]["text"]
        route = json_data["routes"][0]["legs"][0]["steps"][1]["transit_details"]["line"]["url"]

        response = "Instructions: " + instructions +"\nBus: "+ bus + "\nDeparture time: " + departureTime+"\nArrival time: " + arrivalTime+\
                   "\nBus travel time: " + busTravelTime + "\nRoute: " + route

        return response

    def getRouteFrom(self,adress):

        #asking user for destination adress
        formatedURL = "https://maps.googleapis.com/maps/api/" \
                          "directions/json?origin={0}&destination={1}&mode=transit&key={2}".format(self.mctcAdress, adress,
                                                                                                   self.apiKey)
        request = requests.get(formatedURL)
        json_data = json.loads(request.content)
        instructions = json_data["routes"][0]["legs"][0]["steps"][0]["html_instructions"]
        bus = json_data["routes"][0]["legs"][0]["steps"][1]["transit_details"]["headsign"]
        departureTime = json_data["routes"][0]["legs"][0]["steps"][1]["transit_details"]["departure_time"]["text"]
        arrivalTime = json_data["routes"][0]["legs"][0]["steps"][1]["transit_details"]["arrival_time"]["text"]
        busTravelTime = json_data["routes"][0]["legs"][0]["steps"][1]["duration"]["text"]
        route = json_data["routes"][0]["legs"][0]["steps"][1]["transit_details"]["line"]["url"]

        response = "Instructions: " + instructions + "\nBus: " + bus + "\nDeparture time: " + departureTime + "\nArrival time: " + arrivalTime\
                   + "\nBus travel time: " + busTravelTime + "\nRoute: " + route

        return response

#transit = Transit()
#response = transit.getRouteFrom("4130 james avenue north")
#print(response)





