import json

#Open JSON file and load its data
with open("states.json") as f:
    data = json.load(f)

# for state in data["states"]:
#     print(state["name"], state["abbreviation"])

#delete the area_codes items
for state in data["states"]:
    del state["area_codes"]


with open("new_states.json", "w") as f:
    json.dump(data, f, indent=2)