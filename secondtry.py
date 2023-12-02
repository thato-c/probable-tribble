import json
import requests

def isList(extractedValue):
        for item in extractedValue:
            returnDictionaryValues(item)

def returnDictionaryValues(extractedValue):
    for key, value in extractedValue.items():
        if isinstance(value, dict):
            print(f"==={key}===")
            returnDictionaryValues(value)
        elif isinstance(value, list):
            isList(value)
        else:
            print(f"{key}: {value}")

# Retrieve the data from the source
url = 'https://api.nasa.gov/neo/rest/v1/feed?start_date=2015-09-07&end_date=2015-09-08&api_key=DEMO_KEY'

try:
    response = requests.get(url)
    response.raise_for_status()
    data = json.loads(response.text)
    returnDictionaryValues(data)

    # Return the key-value pair
    # if value is dictionary call myself again
    # if value is list call list to go to next item
    # else return key-value pair
    

except requests.exceptions.RequestException as e:
    print(f"Error: {e}")