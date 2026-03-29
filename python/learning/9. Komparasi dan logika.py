# membuat gabungan area rentang dari angka

inputUser = float(input('Masukkan angka yang bernilai\nkurang dari 3\natau\nlebih besar dari 10\n'))

# memeriksa angka kurang dari 3
IsKurangDari = (inputUser < 3)
print('Kurang dari 3 =',IsKurangDari)

# memeriksa angka lebih dari 10
ISLebihDari = (inputUser > 10)
print('Lebih dari 10 =',ISLebihDari)


isCorrect = IsKurangDari or ISLebihDari
print('Angka yang anda masukkan; ', isCorrect)

# ------3+++++++++10--------
# kasus irisan
print('\n',10*'=','\n')
inputUser = float(input('Masukkan angka yang bernilai\nlebih dari 3\ndan\nkurang dari 10\n'))
# -------3++++++++
ISLebihDari = (inputUser > 3)
print('Lebih dari 10 =',ISLebihDari)

# ++++++++10-------
IsKurangDari = (inputUser < 10)
print('Kurang dari 3 =',IsKurangDari)


