import json

# persons = {
#     'Michael': 'Johnson',
#     'John': 'Michaels',
#     'interests': ('books', 'basketball',),
# }
#
#
# print(persons)
# print(type(persons))
# r = json.dumps(persons)
# print(r)
# print(type(r))


json_var = '{"Michael": "Johnson", "John": "Michaels", "interests": ["books", "basketball"]}'

print(type(json_var))
r = json.loads(json_var)
print(r)
print(type(r))