import json
import requests

# Retrieve the data from the source
url = 'https://api.nasa.gov/neo/rest/v1/feed?start_date=2015-09-07&end_date=2015-09-08&api_key=DEMO_KEY'

try:
    response = requests.get(url)
    response.raise_for_status()
    data = json.loads(response.text)

    for key, value in data.items():
        print(f"{key}: {value}")

except requests.exceptions.RequestException as e:
    print(f"Error: {e}")