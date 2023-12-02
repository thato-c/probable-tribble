# Documentation
import json
import requests

#print values function
#open dictionary function

def myDictionaryFunction(extractedValue):
        if isinstance(extractedValue, dict):
            isDictionary(extractedValue)
        elif isinstance(extractedValue, list):
            isList(extractedValue)
        else:
            print(extractedValue)

def isList(extractedValue):
    for item in extractedValue:
        myDictionaryFunction(item)

def isDictionary(extractedValue):
    for key, value in extractedValue.items():
        print(f"{key}")
        myDictionaryFunction(value)

# Retrieve the data from the source
url = 'https://api.nasa.gov/neo/rest/v1/feed?start_date=2015-09-07&end_date=2015-09-08&api_key=DEMO_KEY'

try:
    response = requests.get(url)
    response.raise_for_status()
    data = json.loads(response.text)
    #print(data)
    myDictionaryFunction(data)

except requests.exceptions.RequestException as e:
    print(f"Error: {e}")