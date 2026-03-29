#include <iostream> // Untuk input/output. Pustaka ini menyediakan fungsi dan objek yang diperlukan untuk melakukan operasi input dan output dalam program C++.
#include <string> // Untuk menggunakan std::string

/* Pustaka iostream berada dalam namespace std. Oleh karena itu, Anda perlu menggunakan std:: 
sebelum objek atau fungsi yang didefinisikan dalam pustaka ini, kecuali jika Anda menggunakan pernyataan using namespace std;.*/
using namespace std; 
// Namespace adalah cara untuk mengelompokkan nama-nama yang digunakan dalam program. Dengan menggunakan namespace, 

/* Anda dapat memiliki dua atau lebih entitas dengan nama yang sama di dalam program yang sama tanpa menyebabkan konflik.
contoh nama metode yang sama dengan namepsace yang berbeda */ 
namespace NamespaceA {
    // void adalah cara untuk mendeklarasikan fungsi tanpa nilai kembali atau yang tidak mengembalikan nilai     
    void display() {
        cout << "Ini dari NamespaceA" << endl;
    }
}
namespace NamespaceB {
    void display() {
        cout << "Ini dari NamespaceB" << endl;
    }
}

int test(){
    int angka;
    cout << "Masukkan angka positif: ";// Data disimpan dalam buffer
    cin >> angka ;
    if(angka<0){
        cout << "Anda memasukkan angka negatif" << endl;// Buffer dikosongkan
        return angka;
    }
    cout << "Anda memasukkan angka " << angka << endl;// Buffer dikosongkan
    return angka;
}

/* main() harus memiliki tipe kembali int. 
Ini digunakan untuk mengindikasikan status eksekusi program kepada sistem operasi.*/
int main(){
    cout << "Hello world" << endl;
    cout << "Masukkan nama anda: " << endl;
    string nama;
    cin >> nama ;
    cout << "Nama saya adalah " << nama << endl;
    int angka;
    angka = test();
    cout << "Angka yang diinput di fungsi sebelumnya adalah" << angka << endl;
    NamespaceA::display(); // Memanggil fungsi dari NamespaceA
    NamespaceB::display(); // Memanggil fungsi dari NamespaceB
    return 0;
}

