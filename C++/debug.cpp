#include <iostream>

#define DEBUG // Mendefinisikan makro DEBUG

/*Dengan #define DEBUG: Anda dapat mengontrol apakah pernyataan debug dieksekusi atau tidak. Jika DEBUG tidak didefinisikan, 
pernyataan debug tidak akan dikompilasi dan tidak akan muncul dalam output.*/

void someFunction() {
    // Kode utama fungsi
    std::cout << "Fungsi dijalankan." << std::endl;

#ifdef DEBUG // Memeriksa apakah DEBUG didefinisikan
    std::cout << "Debugging informasi: Fungsi someFunction dipanggil." << std::endl;
#endif
}

int main() {
    someFunction();
    return 0;
}