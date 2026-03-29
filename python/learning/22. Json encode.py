import json

person_dict = {'name': "Rizki",
"No Rekening": "12345",
"saldo": 5500000,
}

#with open('data_nasabah.json', 'w') as json_file:
 # json.dump(person_dict, json_file)



with open('ara.json','w') as json_file:
  json.dump(person_dict,json_file)