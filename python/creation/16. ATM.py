# INI ADALAH ATM
import json

with open(r"C:\Users\lenovo\Latihan\data_nasabah.json") as file_object:
        data = json.load(file_object)

regis = False
while not regis:
    no_rekening = str(input("Masukkan no rekening anda\t:\n"))
    if no_rekening == data['Nasabah_1']['No Rekening']:
        saldo = data['Nasabah_1']['saldo']
        print('\n',10*'=','\n')
        print("SELAMAT DATANG DI ATM", data['Nasabah_1']['nama'])
        print('\n',10*'=','\n')
        regis = True
    elif no_rekening == data['Nasabah_2']['No Rekening']:
        saldo = data['Nasabah_2']['saldo']
        print('\n',10*'=','\n')
        print("SELAMAT DATANG DI ATM", data['Nasabah_2']['nama'])    
        print('\n',10*'=','\n')
        regis = True
    else:
        print("no rekening tidak terdaftar")
        regis = False


print("Silahkan pilih menu\t :\n1.Cek Saldo\n2.Transfer\n3.Tarik Tunai\n4.Setor Tunai\n")

done = False
while not done:
    choice = str(input("Pilih :"))
    if (choice == "1"):
        print('\n',10*'=','\n')
        print("Saldo anda",data['saldo'])
        print('\n',10*'=','\n')
        print(str("1.Keluar\n2.Menu\n"))
        done_2 = False
        while not done_2:
            choice_2 = str(input("Pilih:"))
            if (choice_2 == "1"):
                done_2 = True
                done = True
            elif (choice_2 == "2"):
                print('\n',10*'=','\n')
                print("Silahkan pilih menu\t :\n1.Cek Saldo\n2.Transfer\n3.Tarik Tunai\n4.Setor Tunai\n")
                done_2 = True
                done = False
            else:
                print("Perintah tidak dikenali")
                print('\n',10*'=','\n')
                print("Silahkan pilih menu\t :\n1.Cek Saldo\n2.Transfer\n3.Tarik Tunai\n4.Setor Tunai\n")
                done_2 = True
                done = False
    elif (choice == "2"):
        print('\n',10*'=','\n')
        print("Transfer ke:\n1.Antar Rekening\n2.Antar Bank\n")
        print('\n',10*'=','\n')
        done_3 = False
        while not done_3:
            choice_3 = str(input("Pilih:"))
            if (choice_3 == "1"):
                Rekening = (str(input("Masukkan No Rekening\t:\n")))
                Jumlah = (int(input("Masukkan Jumlah\t:\n")))
                print('\n',10*'=','\n')
                print("Konfirmasi (Y/N)\t:\n")
                print('\n',10*'=','\n')
                konfirmasi = False
                while not konfirmasi:
                    choice_4 = str(input("Pilih:"))
                    if (choice_4 == "Y"):
                        cukup_2 = False
                        while not cukup_2:
                            if (saldo - Jumlah < 0):
                                print('\n',10*'=','\n')
                                print("Saldo anda tidak cukup")
                                print('\n',10*'=','\n')
                                print("Silahkan pilih menu\t :\n1.Cek Saldo\n2.Transfer\n3.Tarik Tunai\n4.Setor Tunai\n")
                                cukup_2 = True
                                konfirmasi = True
                                done_3 = True
                                done = False
                            else:
                                print('\n',10*'=','\n')
                                print("Transfer berhasil")
                                saldo -= Jumlah
                                print ("Saldo tersisa",saldo)
                                new_data = {'saldo':saldo}
                                data.update(new_data)
                                with open('data_nasabah.json', 'w') as json_file:
                                    json.dump(data, json_file)
                                print('\n',10*'=','\n')
                                print(str("1.Keluar\n2.Menu\n"))
                                exit_transfer1 = False
                                while not exit_transfer1:
                                    choice_5 = str(input("Pilih:"))
                                    if (choice_5 == "1"):
                                        exit_transfer1 = True
                                        cukup_2 = True
                                        konfirmasi = True
                                        done_3 = True
                                        done = True
                                    elif (choice_5 == "2"):
                                        print('\n',10*'=','\n')
                                        print("Silahkan pilih menu\t :\n1.Cek Saldo\n2.Transfer\n3.Tarik Tunai\n4.Setor Tunai\n")
                                        exit_transfer1 = True
                                        cukup_2 = True
                                        konfirmasi = True
                                        done_3 = True
                                        done = False
                                    else:
                                        print('\n',10*'=','\n')
                                        print("Perintah tidak dikenali")
                                        print('\n',10*'=','\n')
                                        print("Silahkan pilih menu\t :\n1.Cek Saldo\n2.Transfer\n3.Tarik Tunai\n4.Setor Tunai\n")
                                        exit_transfer1 = True
                                        cukup_2 = True
                                        konfirmasi = True
                                        done_3 = True
                                        done = False
                    elif (choice_4 == "N"):
                        print('\n',10*'=','\n')
                        print("Silahkan pilih menu\t :\n1.Cek Saldo\n2.Transfer\n3.Tarik Tunai\n4.Setor Tunai\n")
                        konfirmasi = True
                        done_3 = True
                        done = False
            elif (choice_3 == "2"):
                print("Transfer antar Bank akan dikenakan biaya admin sebesar RP.5000")
                print('\n',10*'=','\n')
                print("Konfirmasi (Y/N)")
                print('\n',10*'=','\n')
                konfirmasi_2 = False
                while not konfirmasi_2:
                    choice_6 = str(input("Pilih:"))
                    if (choice_6 == "Y"):
                        Rekening_2 = (str(input("Masukkan No Rekening\t:\n")))
                        Jumlah_2 = (int(input("Masukkan Jumlah\t:\n")))
                        print('\n',10*'=','\n')
                        print("Konfirmasi (Y/N)\t:\n")
                        print('\n',10*'=','\n')
                        konfirmasi_3 = False
                        while not konfirmasi_3:
                            choice_7 = str(input("Pilih:"))
                            if (choice_7 == "Y"):
                                print('\n',10*'=','\n')
                                print("Transfer berhasil")
                                saldo = saldo - Jumlah_2 - 5000
                                new_data = {'saldo':saldo}
                                data.update(new_data)
                                with open('data_nasabah.json', 'w') as json_file:
                                    json.dump(data, json_file)
                                print ("Saldo tersisa",saldo)
                                print('\n',10*'=','\n')
                                print("Silahkan pilih menu\t :\n1.Cek Saldo\n2.Transfer\n3.Tarik Tunai\n4.Setor Tunai\n")
                                konfirmasi_3 = True
                                konfirmasi_2 = True
                                done_3 = True
                                done = False
                            elif (choice_7 == "N"):
                                print('\n',10*'=','\n')
                                print("Transfer ke:\n1.Antar Rekening\n2.Antar Bank\n")
                                konfirmasi_3 = True
                                konfirmasi_2 = True
                                done_3 = False
                            else:
                                print('\n',10*'=','\n')
                                print("Perintah tidak dikenali")
                                print('\n',10*'=','\n')
                                print("Silahkan pilih menu\t :\n1.Cek Saldo\n2.Transfer\n3.Tarik Tunai\n4.Setor Tunai\n")
                                konfirmasi_3 = True
                                konfirmasi_2 = True
                                done_3 = True
                                done = False
                    elif (choice_6 == "N"):
                        print('\n',10*'=','\n')
                        print("Silahkan pilih menu\t :\n1.Cek Saldo\n2.Transfer\n3.Tarik Tunai\n4.Setor Tunai\n")
                        exit_transfer2 = True
                        konfirmasi_2 = True
                        done_3 = True
                        done = False
                    else:
                        print('\n',10*'=','\n')
                        print("Perintah tidak dikenali")
                        print('\n',10*'=','\n')
                        print("Silahkan pilih menu\t :\n1.Cek Saldo\n2.Transfer\n3.Tarik Tunai\n4.Setor Tunai\n")
                        konfirmasi_2 = True
                        done_3 = True
                        done = False
            else:
                print("Perintah tidak dikenali")
                print('\n',10*'=','\n')
                print("Silahkan pilih menu\t :\n1.Cek Saldo\n2.Transfer\n3.Tarik Tunai\n4.Setor Tunai\n")
                done_3 = True
                done = False
    elif (choice == "3"):
        print("Silahkan masukkan nominal :\n")
        Jumlah_3 = int(input())
        print('\n',10*'=','\n')
        print("Konfirmasi (Y/N)?")
        tarik = False
        while not tarik:
            choice_8 = str(input("Pilih :"))
            if (choice_8 == "Y"):
                cukup = False
                while not cukup:
                    if (saldo - Jumlah_3 < 0):
                        print('\n',10*'=','\n')
                        print("Saldo anda tidak cukup")
                        print('\n',10*'=','\n')
                        print("Silahkan pilih menu\t :\n1.Cek Saldo\n2.Transfer\n3.Tarik Tunai\n4.Setor Tunai\n")
                        cukup = True
                        tarik = True
                        done = False
                    else:  
                        print('\n',10*'=','\n')
                        print("Tarik tunai berhasil\nSilahkan ambil uang anda")       
                        saldo = saldo - Jumlah_3
                        new_data = {'saldo':saldo}
                        data.update(new_data)
                        with open('data_nasabah.json', 'w') as json_file:
                            json.dump(data, json_file)
                        print("Sisa saldo anda\t:",saldo)
                        print('\n',10*'=','\n')
                        print(str("1.Keluar\n2.Menu\n"))
                        exit_transfer3 = False
                        while not exit_transfer3:
                            choice_9 = str(input("Pilih :"))
                            if (choice_9 == "1"):
                                exit_transfer3 = True
                                cukup = True
                                tarik = True
                                done = True
                            elif (choice_9 == "2"):
                                print("Silahkan pilih menu\t :\n1.Cek Saldo\n2.Transfer\n3.Tarik Tunai\n4.Setor Tunai\n")
                                exit_transfer3 = True
                                cukup = True
                                tarik = True
                                done = False
                            else:  
                                print('\n',10*'=','\n')
                                print("Perintah tidak dikenali")
                                print('\n',10*'=','\n')
                                print(str("1.Keluar\n2.Menu\n"))
                                exit_transfer3 = False
            elif (choice_9 == "N"):
                print('\n',10*'=','\n')
                tarik = True
                done = False
            else:
                print("Perintah tidak dikenali")
                tarik = True
                done = False
    elif (choice == "4"):
        print("Silahkan taruh uang anda :\n")
        Jumlah_4 = int(input())
        print('\n',10*'=','\n')
        print("Konfirmasi (Y/N)?")
        setor = False
        while not setor:
            choice_10 = str(input("Pilih :"))
            if (choice_10 == "Y"):
                print('\n',10*'=','\n')
                print("Setor tunai berhasil\n")       
                saldo = saldo + Jumlah_4
                new_data = {'saldo':saldo}
                data.update(new_data)
                with open('data_nasabah.json', 'w') as json_file:
                    json.dump(data, json_file)
                print("Sisa saldo anda\t:",saldo)
                print('\n',10*'=','\n')
                print(str("1.Keluar\n2.Menu\n"))
                exit_setor = False
                while not exit_setor:
                    choice_11 = str(input("Pilih :"))
                    if (choice_11 == "1"):
                        exit_setor = True
                        setor = True
                        done = True
                    elif (choice_11 == "2"):
                        print("Silahkan pilih menu\t :\n1.Cek Saldo\n2.Transfer\n3.Tarik Tunai\n4.Setor Tunai\n")
                        exit_setor = True
                        setor = True
                        done = False
                    else:  
                        print('\n',10*'=','\n')
                        print("Perintah tidak dikenali")
                        print('\n',10*'=','\n')
                        print("Silahkan pilih menu\t :\n1.Cek Saldo\n2.Transfer\n3.Tarik Tunai\n4.Setor Tunai\n")
                        exit_setor = True
                        setor = True
                        done = False
            elif (choice_10 == "N"):
                print("Silahkan pilih menu\t :\n1.Cek Saldo\n2.Transfer\n3.Tarik Tunai\n4.Setor Tunai\n")
                setor = True
                done = False
            else:  
                print('\n',10*'=','\n')
                print("Perintah tidak dikenali")
                print('\n',10*'=','\n')
                print("Silahkan pilih menu\t :\n1.Cek Saldo\n2.Transfer\n3.Tarik Tunai\n4.Setor Tunai\n")
                setor = False
                done = False
    else:
        print("Perintah tidak dikenali")
        done = True
