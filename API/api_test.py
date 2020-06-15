import urllib.request
import json

with open('keys.env') as f:
    api_key = '&key=' + f.readline()
    f.close()

print(api_key)

#address = 'origin={20148}'
address = 'address=20148'
#address = 'address=23984+Lavender+Meadow+Pl,+Ashburn,+VA'
destination = '&destination={20152}'
#main_api = 'https://maps.googleapis.com/maps/api/directions/json?'
main_api = 'https://maps.googleapis.com/maps/api/geocode/json?'

#url = main_api + address + destination + api_key
url = main_api + address + api_key

request = url
response = urllib.request.urlopen(request).read()
directions = json.loads(response)

#json_data = requests.get(url).json()

#print(json_data)

#response_json = response.json()

print(json.dumps(directions, indent=4, sort_keys=True))