
import urllib

import requests
import json


#r = requests.get('https://api.github.com/user', auth=('storagedevops', 'LedZeppelin3577!'))
#r = requests.get('https://api.github.com/events')
#response = r.json()

#print(json.dumps(response, indent=4, sort_keys=True))

#request = requests.get('http://api.open-notify.org')
#print(request.text)

people = requests.get('http://api.open-notify.org/astros.json')
people_json = people.json()
#print(json.dumps(people_json, indent=4, sort_keys=True))
print("Number of people in space:", people_json['number'])
