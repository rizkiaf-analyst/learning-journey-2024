a = 9
b = 5

# operator OR (|)
c = a | b

print(5*'=','OR','='*5)

print('nilai :', a, ' , binary :',format(a,'08b'))
print('nilai :', b, ' , binary :',format(b,'08b'))

print('----------(|)')
print('nilai :', c, ' , binary :',format(c,'08b'))


# operator and (&)
c = a & b

print(5*'=','AND','='*5)

print('nilai :', a, ' , binary :',format(a,'08b'))
print('nilai :', b, ' , binary :',format(b,'08b'))

print('----------(&)')
print('nilai :', c, ' , binary :',format(c,'08b'))

# operator XOR (^)
c = a ^ b

print(5*'=','XOR','='*5)

print('nilai :', a, ' , binary :',format(a,'08b'))
print('nilai :', b, ' , binary :',format(b,'08b'))

print('----------(XOR)')
print('nilai :', c, ' , binary :',format(c,'08b'))


#bitwise NOT (~)
c = ~a

print(5*'=','NOT','='*5)

print('nilai :', a, ' , binary :',format(a,'08b'))

print('----------(NOT)')
print('nilai :', c, ' , binary :',format(c,'08b'))
print('nilai :', c, ' , binary :',format(c&0xFF,'08b'))
bin = 0b11110110
print("nilai binary 11110110 =",bin)

print('----------(FLIP)')
# operasi flip 
d = 0b00101110
e = 0b00001001
print('nilai d:',d,'nilai e:',e)
print('nilai :',d^e,' , binary :',format(d^e,'08b'))



# shifting
# shift right (>>)
print('===========(>>)')
c = a >> 2

print('nilai :', a, ' , binary :',format(a,'08b'))

print('----------(>>)')
print('nilai :', c, ' , binary :',format(c,'08b'))

c = a << 2

print('===========(<<)')
print('nilai :', a, ' , binary :',format(a,'08b'))

print('----------(<<)')
print('nilai :', c, ' , binary :',format(c,'08b'))
