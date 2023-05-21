import json
# JSON can be parse using json.loads() method

# creating JSON
new_json = '{"course":"python", "duration":"2 months"}'
print(type(new_json))

# converting json into dictionary
new_types = json.loads(new_json)
print(new_types)
# to get the type of new_types
print(type(new_types))
