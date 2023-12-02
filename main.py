# Documentation
import requests

source = requests.get('https://api.nasa.gov/neo/rest/v1/feed?start_date=2015-09-07&end_date=2015-09-08&api_key=DEMO_KEY')
print(source.status_code)
print("")
print(source.json())