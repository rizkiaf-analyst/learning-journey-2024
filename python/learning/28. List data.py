# Mengenal list dengan urutan, list pertama = 0
buah = ["apel", "anggur", "mangga", "jeruk"]
print(buah[3])

# Memanggil data dari list dengan urutan, sisip dalam string
my_friends = ["Anggun", "Dian", "Agung", "Adi", "Adam"]
print("Isi my_friends indeks ke-3 adalah: {}".format(my_friends[3]))

print("Semua teman: ada {} orang".format(len(my_friends)))
for friend in my_friends:
    print(friend)

# Memanggil data perhitungan dari list dengan urutan, sisip dalam string
a = 2
b = 3
hasil = [a + b, 30]
print("Hasil penjumlahan 2+3\t: {}".format(hasil[0]))

# Mengganti list data

# list mula-mula
buah = ["jeruk", "apel", "mangga", "duren"]
# mengubah nilai index ke-2
buah[2] = "kelapa"

print(buah)

#prepend(item) menambahkan item dari depan;
#append(item) menambahkan item dari belakang.
#insert(index, item) menambahkan item dari indeks tertentu

#list mula-mula
buah = ["jeruk", "apel", "mangga", "duren"]
# Tambahkan manggis
buah.append("manggis")
#buah.prepend("jambu")

print(buah)

#Cara menambahkan item di akhir dan dari indeks tertentu
#Perintah dapat disatukan dalam satu variabel
warna = ["hitam", "putih", "hijau", "biru"]
warna.insert(2, "ungu")
warna.append("orange")

print(warna)


# Membuat list kosong untuk menampung hobi
hobi = []
stop = False
i = 0

# Mengisi hobi
while(not stop):
    hobi_baru = input("Inputkan hobi yang ke-{}: ".format(i))
    hobi.append(hobi_baru)

    # Increment i
    i += 1
    
    tanya = input("Mau isi lagi? (y/t): ")
    if(tanya == "t"): 
        stop = True


# Cetak Semua Hobi
print("=" * 10)
print("Kamu memiliki {} hobi".format(len(hobi)))
for hb in hobi:
    print("- {}".format(hb))


listnamabulan = ['Januari','Februari','Maret']
for wow in listnamabulan:
    print(wow)
print('Januari' in listnamabulan)



bulan = ["januari","februari","maret","april"]
bulan.insert(2,"desember")
for i in enumerate(bulan):
    print(i)

# while untuk menampilkan isi list 

listhari = ['senin','selasa','rabu','kamis','jumat','sabtu','minggu']

i = 0
while i < len(listhari):
    print(listhari[i])
    i += 1