#contoh tipe variabel global dan variabel lokal pada variabel "provinsi"

kota, provinsi = 'Lamongan', 'Jawa Timur'

def hello ():
  #global provinsi
  provinsi = 'Jawa Barat'
  print(kota, provinsi)

print('[PANGGIL FUNGSI hello()]')
hello()


print('\n[SECARA LANGSUNG]')
print(kota, provinsi)


#Docstring (memberikan keterangan pada sebuah fungsi)

def suhu_udara (daerah, derajat = 30, satuan = 'celcius'):
  """
  Fungsi ini bertugas untuk menampilkan teks yang memberikan informasi 
  tentang suhu udara di suatu daerah.
  """

  print("Suhu di {} adalah {} {}".format(daerah, derajat, satuan))

suhu_udara("jombang", satuan = "celcius")

def tampilkanAngka (batas, i = 1):
  print(f'Perulangan ke {i}')

# Panggil beberapa kali untuk mensimulasikan
# cara kerja
tampilkanAngka(3)
tampilkanAngka(3, 2)
tampilkanAngka(5, 3)


def harga_setelah_pajak(harga_dasar):
    return harga_dasar + (harga_dasar *10/100)


harga_cilok = 5000

harga_final_cilok = harga_setelah_pajak(harga_cilok)
print("Harga cilok 1 porsi Rp.", harga_final_cilok)