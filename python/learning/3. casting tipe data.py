data_int = 6
print("data =", data_int, "type =", type(data_int))

data_float = float(data_int)
data_str = str(data_int)
data_bool = bool(data_int)

print("data =", data_float, "type =", type(data_float))
print("data =", data_str, "type =", type(data_str))
print("data =", data_bool, "type =", type(data_bool))

print("=====FLOAT=====")

data_float = 6.2
print("data =", data_float, "type =", type(data_float))

data_int = int(data_float)
data_str = str(data_float)
data_bool = bool(data_float)

print("data =", data_int, "type =", type(data_int))
print("data =", data_str, "type =", type(data_str))
print("data =", data_bool, "type =", type(data_bool))

print("=====STRING=====")
data_string = "0"
print("data =", data_string, "type =", type(data_string))

data_int = int(data_string)
data_bool = bool(data_string)
print("data =", data_int, "type =", type(data_int))
print("data =", data_bool, "type =", type(data_bool))
print("data =", bool(data_int), "type =", type(bool(data_int)))

print("=====BOOL=====")
data_bool = False
print("data =", data_bool, "type =", type(data_bool))

data_int = int(data_bool)
data_float = float(data_bool)
data_string = str(data_bool)

print("data =", data_int, "type =", type(data_int))
print("data =", data_float, "type =", type(data_float))
print("data =", data_string, "type =", type(data_string))
  
print("=====COMPLEXX=====")

data_int = 5
data_complex = complex(data_int)
print("data =", data_complex, "type =", type(data_complex))