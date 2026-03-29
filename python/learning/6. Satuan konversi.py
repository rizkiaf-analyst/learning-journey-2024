#latihan konversi satuan temperature

#program konversi celcius ke satuan lain

print("\nPROGRAM KONVERSI TEMPERATURE CELCIUS\n")

celcius = float(input('Masukan suhu dalam celcius : '))
print("Suhu adalah : ", celcius, "C")

# reamur
reamur = (4/5) * celcius
print("Suhu dalam reamur adalah ", reamur, "R")

# fahrenheit
fahrenheit = ((9/5) * celcius) + 32
print("Suhu dalam fahrenheit adalah : ", fahrenheit, "F")


# kelvin
kelvin = celcius + 273
print("Suhu dalam kelvin adalah : ", kelvin, "K")


print("\nPROGRAM KONVERSI TEMPERATURE FAHRENHEIT\n")

fahrenheit = float(input('Masukan suhu dalam fahrenheit : '))
print("Suhu adalah : ", fahrenheit, "F")

# fahrenheit
fahrenheit = ((9/5) * celcius) + 32
celcius = (5*(fahrenheit - 32))/9
print("Suhu dalam celcius adalah : ", celcius, "C")

# kelvin
kelvin = celcius + 273
print("Suhu dalam kelvin adalah : ", kelvin, "K")

print("\nPROGRAM KONVERSI TEMPERATURE KELVIN\n")

kelvin = float(input('Masukan suhu dalam kelvin : '))
print("Suhu adalah : ", kelvin, "K")

# fahrenheit
celcius = kelvin - 273
print("Suhu dalam celcius adalah : ", celcius, "C")
fahrenheit = ((9/5) * celcius) + 32
print("Suhu dalam fahrenheit adalah : ", fahrenheit, "F")
