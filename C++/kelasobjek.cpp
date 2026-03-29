#include <iostream> // Untuk input/output. Pustaka ini menyediakan fungsi dan objek yang diperlukan untuk melakukan operasi input dan output dalam program C++.
#include <string> 

// membuat kelas
class PersegiPanjang{
    private:
        int panjang,lebar; // Deklarasi variabel panjang dan lebar
    public:
        // Konstruktor untuk menginisialisasi panjang dan lebar
        PersegiPanjang(int p, int l): panjang(p), lebar(l) {}

    // Fungsi untuk menghitung luas persegi panjang
    int LuasPersegiPanjang(){
        return panjang*lebar;
    }
    int KelilingPersegiPanjang(){
        return 2*(panjang+lebar);
    }
};

int hitung(int a, int b){
    int max;
    if (a>b) {
        return max = a;
    } else {
        return max = b;
    }
}

void loop(){
    int sum = 0;
    for (int i = 1; i <= 10; i++){
        sum += i;
        std::cout << "index ke-" << i << " dengan nilai sum jadi : " << sum << std::endl;
    }
    std::cout << "Jumlah dari 1 hingga 10 adalah: " << sum << std::endl; // Menampilkan hasil
}


int main() {
    // Contoh penggunaan kelas
    PersegiPanjang pp(5, 3); // Membuat objek PersegiPanjang dengan panjang 5 dan lebar 3
    std::cout << "Luas Persegi Panjang: " << pp.LuasPersegiPanjang() << std::endl; // Menampilkan luas
    std::cout << "Keliling Persegi Panjang: " << pp.KelilingPersegiPanjang() << std::endl; // Menampilkan Keliling
    int a = 5;
    int b = 3;
    int hasil = hitung(a,b);
    std::cout << "Nilai maximal dari hasil adalah : " << hasil << std::endl;
    loop();
    return 0; // Mengembalikan 0 untuk menunjukkan keberhasilan
}