# program menghitung volume dan luas permukaan bola
phi = 3.14
r = float(input("Masukkan jari-jari lingkaran\t: "))

def Volume(r):
    volume = 4/3 * phi * r ** 3
    return volume

def Luas(r):
    Luas = 4 * phi * r ** 3
    return Luas

def main():
    print('Luas bola\t:',Luas(r))
    print('Volume bola\t:',Volume(r))
main()
