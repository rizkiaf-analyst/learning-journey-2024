# ekstraksi nomor telepon

import re

text = 'Hubungi saya di 088134349334 02134349334'
phone_numbers = re.findall(r'\b\d{10,12}\b', text)

print('Nomor Telepon: ', phone_numbers) 


string = "python is a popular python programming language"

pattern = r'^[\w\.-]+'

match = re.search(pattern, string)
if match:
    print('Match found: ', match.group())
else:
    print('No match')

matc = re.findall(pattern,string)
print(matc)


text = "kamu suka apel"
regex = re.findall(r"kakaka",text)
print(bool(regex))


