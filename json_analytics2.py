import json

#define a custom sorting function.
def install_sort(package):
    return package["analytis"]["30d"]

#load json from the file.
with open("package_info.json", "r") as f:
    data = json.load(f)

data = [item for item in data if 'video' in item['desc']] #filter to get package with 'video' in description.

data.sort(key=install_sort, reverse=True)

data_str = json.dumps(data[:5], indent=2) #get only the first 5 packages