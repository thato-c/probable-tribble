# File that decodes JSON data so that it could be inspected before creating tables

import json
import requests

tableNames = set()
columnNames = ''
rowValues =  ''

def isList(extractedValue):
        for item in extractedValue:
            returnDictionaryValues(item)

def returnDictionaryValues(extractedValue):
    global tableNames, columnNames

    try:
        for key, value in extractedValue.items():
            if isinstance(value, dict):
                #print(f"==={key}===")
                tableNames.add(key)
                returnDictionaryValues(value)
            elif isinstance(value, list):
                isList(value)
            else:
                #print(f"{key}: {value}")
                columnNames += f"{key}\n"
                #rowValues += f"{value}"

    except AttributeError as e:
        print(f"{extractedValue}")


# Retrieve the data from the source
NeowsUrl = 'https://api.nasa.gov/neo/rest/v1/feed?start_date=2015-09-07&end_date=2015-09-08&api_key=DEMO_KEY'

try:
    response = requests.get(NeowsUrl)
    response.raise_for_status()
    data = json.loads(response.text)
    returnDictionaryValues(data)
    print("")
    print("======================================")
    print("")
    print(tableNames)
    print(columnNames)

except requests.exceptions.RequestException as e:
    print(f"Error: {e}")