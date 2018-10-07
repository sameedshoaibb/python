# // How to load json string to python object
import json
import logging

people_string='''
{
	"people":
	[
 		{
 		  "name":"sameed",
 		  "phone":"03422020091"
 		},
 		{
 		  "name":"jawad",
 		  "phone":"03452541419",
 		  "has_liscence": true
 		}
	]
}
'''

data=json.loads(people_string)
# //load(s) will load a string and (load) will load a file in python object
print data

for person in data['people']:
	print person
	print person['name']

# // Dump python object to json string, remove the name nad then convert it back to python string
	del person['name']
	print person
new_data=json.dumps(data,indent=2, sort_keys=True)
print "This is the modified data",new_data

                                # How to load json file into python object

 import json
 
 # //To load a file, first open it 
 with open('states.json') as e:
     data=json.load(e)  #load it into python object 

for state in data['states']:	# loop through a data
	print state
	print state['name']
	del area['area_codes'] # //Write this python object out to file
 	# To write this file as json, we use json.dump )Dump method will convert data into json file)
 with open('new_states','w') as g:
	 json.dump(data,g,indent=2) #pass the data that want to dump	


								# Fetch data from API and perform the desired action
import json
from urllib.request import urlopen

with urlopen("https://finance.yahoo.com/webservice/v1/symbols/allcurrencies/quote?format=json") as response:
    source = response.read()

data = json.loads(source)

# print(json.dumps(data, indent=2))

usd_rates = dict()

for item in data['list']['resources']:
    name = item['resource']['fields']['name']
    price = item['resource']['fields']['price']
    usd_rates[name] = price

print(50 * float(usd_rates['USD/INR']))