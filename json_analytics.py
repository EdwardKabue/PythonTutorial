import json
import requests

r = requests.get("https://formulae.brew.sh/api/formula.json") #get content from URL
packages_json = r.json() #get the json encoded content

packages_str = json.dumps(packages_json[0], indent=2)

print(packages_str)