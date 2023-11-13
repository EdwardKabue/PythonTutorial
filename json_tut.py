import json

people_string = '''
{
    "people": [{
        "name": "John Smith",
        "phone": "678-098-876",
        "emails": ["jsmith@work.com", "smithj@work.com"],
        "has_license": false
    },
    {
        "name": "Jane Doe",
        "phone": "658-090-874",
        "emails": null,
        "has_license": false
    }
]
}
'''

data = json.loads(people_string)
#print(data)
#print(type(data["people"])) #<class 'list'>

#loop through the list of people
for person in data["people"]:
    del person["phone"] #delete items with key 'phone'

new_string = json.dumps(data, indent=2, sort_keys=True) #get the new json string after deleting the phone items
print(new_string)

