# gak ada coma = integer
data_integer = 1
type(data_integer)
print("data : ", data_integer)
print("- bertipe : ", type(data_integer))

#tipe data: float = angka dengan coma
data_float = 1.5
print(type(data_float))

data_string = "ucup"
print(type(data_string))

data_bool = False
print(type(data_bool))

data_bool = "False"
print(type(data_bool))
print(data_bool)

data_complex = complex(6,6)
print("data",data_complex)
print("-bertipe :", type(data_complex))

a = 2
print(a*data_complex)

from ctypes import c_double

data_c_double = c_double(10.5)
print("data",data_c_double)
print("-bertipe :", type(data_c_double))