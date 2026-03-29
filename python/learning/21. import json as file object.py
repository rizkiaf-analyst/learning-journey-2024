import json

with open(r"C:\Users\lenovo\Latihan\data_nasabah.json") as file_object:
        data = json.load(file_object)



print(data)
print(data['Nasabah_1'])

value = data.get('Nasabah_6',"Nasabah tidak ditemukan")
print(value)