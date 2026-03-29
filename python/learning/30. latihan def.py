def selamat_datang (nama):
  print(f'Halo {nama}, selamat datang!')

selamat_datang('Nurul')
selamat_datang('Lendis')
selamat_datang('Fabri')
selamat_datang('isa')

def perkenalan(nama, asli):
  print(f"Perkenalkan saya {nama} dari {asli}")

perkenalan("ucup","bandung")

def suhu_udara(daerah, derajat, satuan='celcius'):
  print(f"Suhu di {daerah} adalah {derajat} {satuan}")

suhu_udara("Surabaya", 30)
suhu_udara("Surabaya", 86, 'Fahrenheit')




def luas_persegi (sisi):
  return sisi * sisi

persegi_besar = luas_persegi(100)
persegi_kecil = luas_persegi(50)

print("luas persegi adalah\t:", luas_persegi(10))
print('Toal luas persegi besar dan kecil adalah:', persegi_besar + persegi_kecil)


def persentase (total, jumlah):
  if (total >= 0 and total <= jumlah):
    return total / jumlah * 100
  
  return False

print(persentase(30, 60))
print(persentase(100, 60))

total = 30
jumlah = 60
if (total >= 0 and total <= jumlah):
  ppersentase = total / jumlah * 100
  print(ppersentase)
else:
  print(False)

total = 100
jumlah = 60
if (total >= 0 and total <= jumlah):
  ppersentase = total / jumlah * 100
  print(ppersentase)
else:
  print(False)

