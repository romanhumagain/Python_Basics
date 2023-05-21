import json
#JSON -> JavaScript Object Notation
# JSON is used for storing and transferring data between the browser and the server
# JSON is the text, writtebn with javasript object notation
# JSON supports mainly 6 data types

'''
>string     >number
>boolean    >null
>object     >array
'''

# In python JSON exixts as string
new_json = '{"name":"roman ", "course":"Software Engineer"}'
print(type(new_json))

# creating dictionary and converting to json
# .dumps() function is used to convert
new_dict = {"URL":"romanhumagain.com.np", "name":"Roman Humagain"}
new_json = json.dumps(new_dict)
print(new_json)
print(type(new_json))