alas = int(input("Masukkan alas: "))
tinggi = int(input("Masukkan tinggi: "))

def hitung():
    luas = 0.5 * alas * tinggi
    return luas

def main():
    print("Luas Segitiga:", hitung())
main()


