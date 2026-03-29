# operasi komparasi

# setiap hasil dari operasi komparasi adalah boolean

a = 4
b = 2

#lebih besar dari >
print('===== lebih besar dari (>)')
hasil = a > 3
print(a,'>',3,'=',hasil)

hasil = a < 3
print(a,'<',3,'=',hasil)

#kurang dari >
print('===== kurang besar dari (>)')
hasil = b < 3
print(b,'<',3,'=',hasil)

hasil = b > 3
print(b,'>',3,'=',hasil)

#lebih besar sama dengan >=
print('===== lebih besar sama dengan (>=)')
hasil = a >= 4
print(a,'>=',4,'=',hasil)
hasil = b >= 4
print(b,'>=',4,'=',hasil)
hasil = b >= 2
print(b,'>=',2,'=',hasil)


print('===== sama dengan (==)')
hasil = a == 4
print(a,'==',4,'=',hasil)
hasil = a == 5
print(a,'==',5,'=',hasil)


print('===== tidak sama dengan (!=)')
hasil = a != 4
print(a,'!=',4,'=',hasil)
hasil = a != 5
print(a,'!=',5,'=',hasil)

# 'is' sebagai komparasi object identity
x = 5 # ini adalah assignment membuat object
y = 10
print(type(x))
print('nilai x =',x,'id = ',hex(id(x)))
print('nilai y =',y,'id = ',hex(id(y)))

hasil = x is y
print('x is y =',hasil)
hasil = x is not y
print('x is y =',hasil)
