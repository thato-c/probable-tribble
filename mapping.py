import json
import requests


def analyze_json_structure(data, indent=0, parent_key=None):
    if isinstance(data, dict):
        for key, value in data.items():
            if parent_key is not None:
                current_key = f"{parent_key}.{key}"
            else:
                current_key = key

            #print("  " * indent + f"Table: {current_key}, Type: {type(value)}")
            analyze_json_structure(value, indent + 1, current_key)
    elif isinstance(data, list):
        for index, item in enumerate(data):
            current_key = f"{parent_key}[{index}]"
            #print("  " * indent + f"Key: {current_key}, Type: {type(item)}")
            analyze_json_structure(item, indent + 1, current_key)
    else:
        print("  " * indent + f"Key: {parent_key}, Value: {data}")


# Retrieve the data from the source
NeowsUrl = 'https://api.nasa.gov/neo/rest/v1/feed?start_date=2015-09-07&end_date=2015-09-08&api_key=DEMO_KEY'

try:
    response = requests.get(NeowsUrl)
    response.raise_for_status()
    data = json.loads(response.text)
    analyze_json_structure(data)

except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
