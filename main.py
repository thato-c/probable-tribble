# File that decodes JSON data so that it could be inspected before creating tables

import json
import requests

def isList(extractedValue):
        for item in extractedValue:
            returnDictionaryValues(item)

def isDictionaryOrList(extractedValue):
    if isinstance(extractedValue, dict):
        for key, value in extractedValue.items():
            print(f"==={key}===")
            isDictionaryOrList(value)
    elif isinstance(extractedValue, list):
        isList(extractedValue)
    else:
        returnDictionaryValues(extractedValue)

def returnDictionaryValues(extractedValue):
    for key, value in extractedValue.items():
        print(f"{key}: {value}")

# def returnDictionaryValues(extractedValue):
#     try:
#         for key, value in extractedValue.items():
#             if isinstance(value, dict):

#                 print(f"==={key}===")

#                 returnDictionaryValues(value)
#             elif isinstance(value, list):
#                 isList(value)
#             else:

#                 print(f"{key}: {value}")
#     except AttributeError as e:
#         print(f"{extractedValue}")


# Retrieve the data from the source
NeowsUrl = 'https://api.nasa.gov/neo/rest/v1/feed?start_date=2015-09-07&end_date=2015-09-08&api_key=DEMO_KEY'
DonkiCMEUrl = 'https://api.nasa.gov/DONKI/CME?startDate=yyyy-MM-dd&endDate=yyyy-MM-dd&api_key=DEMO_KEY'
DonkiCMEAUrl = 'https://api.nasa.gov/DONKI/CME?startDate=yyyy-MM-dd&endDate=yyyy-MM-dd&api_key=DEMO_KEY'

try:
    response = requests.get(DonkiCMEUrl)
    response.raise_for_status()
    data = json.loads(response.text)
    isDictionaryOrList(data)

    # Return the key-value pair
    # if value is dictionary call myself again
    # if value is list call list to go to next item
    # else return key-value pair
    

except requests.exceptions.RequestException as e:
    print(f"Error: {e}")