# deklarasi variabel
nama = str(input("Masukkan NIM \t: "))
nama = str(input("Masukkan Nama \t: "))
uts = int(input("Masukkan UTS \t: "))
tugas = int(input("Masukkan tugas \t: "))
uas = int(input("Masukkan UAS \t: "))

#hitung total nilai
total = (uts/100*30) + (tugas/100*20) +(uas/100*50)
print("Total Nilai \t:",total)

#percabangan
if (total>=40) & (uts>=50) & (tugas>=90) & (uas>=60):
    print("Keterangan \t: Lulus")
else:
    print("Keterangan \t: Tidak Lulus")

x =2
result = "Even" if x % 2 == 0 else "Odd"