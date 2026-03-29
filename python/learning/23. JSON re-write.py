import json

with open(r"C:\Users\lenovo\Latihan\data_nasabah.json") as file_object:
        data = json.load(file_object)

print(type(data['Nasabah_2']['No Rekening']))
print(data['Nasabah_2']['No Rekening'])

new_data = {'saldo':5000}
data.update(new_data)

with open('data_nasabah.json', 'w') as json_file:
  json.dump(data, json_file)

print(data)
