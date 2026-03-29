#include <iostream> // Untuk input/output. Pustaka ini menyediakan fungsi dan objek yang diperlukan untuk melakukan operasi input dan output dalam program C++.
#include <string> 

class Bebek {
    public:
        std::string quack() {
            return "Quack!";
        }
};
    
class Anjing {
    public:
        std::string quack() {
            return "Woof!";
        }
};
    
void suara_hewan(Bebek& hewan) {
        std::cout << hewan.quack() << std::endl;  // Harus berupa Bebek
}
   
int main() {
    Bebek bebek;
    Anjing anjing;
    suara_hewan(bebek);  // Valid
    Anjing wolf;
    std::cout << anjing.quack() << std::endl;
    //suara_hewan(anjing);  // Ini akan menyebabkan kesalahan kompilasi
}