import json

json_string = '{"name": "Bob", "languages": ["English", "French"]}'
data = json.loads(json_string)

print(type(data))  # <class 'dict'>
print(data['name'])  # Bob
print(data['languages'])  # ['English', 'French']

for json,value in data.items():
    print(f'{json} & {value}')