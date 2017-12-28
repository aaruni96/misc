import urllib.request
import json

origin = input("Origin\n")
destination = input("Destination\n")
urllib.request.urlretrieve("https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&origins="+origin+"&destinations="+destination,"abc.json")
data=json.load(open("abc.json"))
distance=data["rows"][0]["elements"][0]["distance"]["value"]/1000.0
print(distance,'km')
