#include <iostream> 
#include <string> 
#include <vector>
#include <array>
#include <algorithm>  

int loop(int sum) {
    for (int i = 1; i <= 10; i++) {
        sum += i;
        std::cout << "Index ke-" << i  << " dengan nilai sum menjadi : " << sum << std::endl; 
    } 
    return sum;
}

int tambah(int a, int b){
    return a + b;
}

std::vector<int> generate_list(int n){
    std::vector<int> result;
    for (int i = 1; i <= n;i++){
        result.push_back(i);
    }
    return result;
}

void bubbleSort(std::array<int, 5>&arr,int n) {
    for (int i = 0; i < n-1; i++) {
        for (int j = 0; j < n-i-1; j++) {
            if (arr[j] > arr[j+1]) {
                int temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
            }
        }
    }
}

void modify_array(std::array<int, 5>&arr,int n){
    for (int i=0;i < n;i++){
        arr[i] = 2 * arr[i];
    }
}

void map_array(std::array<int,5>&arr,int n){
    if (n > arr.size()) {
        n = arr.size();  // Atur n ke ukuran array jika lebih besar
    }
    for (int i=0;i<n;i++){
        if (arr[i] <= 2){
            continue;
        }
        arr[i] = 5 * arr[i];
    }
}

void printArrayVector(std::vector<int>& arr) {
    for (int i = 0; i < arr.size(); i++) {
        std::cout << arr[i] << " ";
    }
    std::cout << std::endl;
}

// List comprehension dengan std::transform
void transform(std::vector<int>&arr){
    std::vector<int> squared;
    for (int x : arr){
        (x % 2 == 0) ? squared.push_back(x * x) : void(); // Menambahkan kuadrat x jika x > 5
        std::cout << "Nilai yang masuk untuk nilai(" << x << "):" << std::endl;
        printArrayVector(squared);
    }
    arr = squared;
}

void printArray(const std::array<int, 5>& arr, int n) {
    for (int i = 0; i < n; i++) {
        std::cout << arr[i] << " ";
    }
    std::cout << std::endl;
}

int add(int a, int b) {
    return a + b;
}

int main(){
    int sum = 0;
    sum = loop(sum);
    int n = 15;
    std::cout << "nilai a+b = " << tambah(2,3) << std::endl;
    std::cout << "Hasil sama dengan " << sum << std::endl;
    std::cout << "Membuat list dengan banyaknya data: " << n << std::endl;
    std::vector<int> myList = generate_list(n);
    std::cout << "Hasilnya adalah: " << std::endl;
    for (size_t i = 0; i < myList.size(); i++) {
        std::cout << "Index ke-" << i+1 << ": " << myList[i] << std::endl;  // Mencetak setiap elemen
    }
    std::cout << std::endl;
    int myArray[] = {5, 4, 3, 2, 1};
    /*Tipe Data Statis: C++ adalah bahasa yang statis dan terkompilasi, 
    yang berarti bahwa informasi tentang ukuran array tidak disimpan dalam 
    bentuk yang dapat diakses secara langsung. 
    Ketika Anda mengoper array ke fungsi, informasi tentang ukuran array hilang, 
    dan hanya pointer ke elemen pertama yang dikirim.*/
    int o = sizeof(myArray)/sizeof(myArray[0]);
    std::cout << "Jumlah elemen dalam array: " << o << std::endl;

    // Alternatif: Menggunakan std::array atau std::vector
    std::array<int, 5> myArray2 = {5, 4, 3, 2, 1};
    std::cout << "Jumlah elemen dalam array: " << myArray2.size() << std::endl;

    std::cout << "Array sebelum disort: " << std::endl;
    printArray(myArray2 , o);
    bubbleSort(myArray2, o);
    std::cout << "Array setelah disort: " << std::endl;
    printArray(myArray2 , o);
    std::cout << "Array setelah dimodifikasi: " << std::endl;
    modify_array(myArray2,o);
    printArray(myArray2,o);

    std::cout << "Array setelah dimodifikasi untuk nilai lebih dari 2: " << std::endl;
    map_array(myArray2,o);
    printArray(myArray2,o);

    std::cout << "Mylist sebelum dimodifikasi: " << std::endl;
    std::vector<int> myList3 = generate_list(5);
    printArrayVector(myList3);
    std::cout << "Mylist setelah dimodifikasi untuk nilai genap saja: " << std::endl;
    transform(myList3);
    std::cout << "Result: " << std::endl;
    printArrayVector(myList3);




    int y = 20;        // Variabel y menyimpan nilai 20
    int* p = &y;      // Pointer p menyimpan alamat dari y
    std::cout << "Nilai y: " << y << std::endl;        // Output: 20
    std::cout << "Nilai melalui pointer p: " << *p << std::endl;  // Output: 20

    *p = 30;  // Mengubah nilai y melalui pointer p
    std::cout << "Nilai y setelah diubah melalui pointer: " << y << std::endl;  // Output: 30

    int* dynamicVar = new int;  // Mengalokasikan memori untuk integer
    *dynamicVar = 40;           // Mengubah nilai yang disimpan di alamat tersebut
    std::cout << "Nilai dari dynamicVar: " << *dynamicVar << std::endl;  // Output: 40
    delete dynamicVar;          // Menghapus alokasi memori
    std::cout << "Nilai dari dynamicVar setelah didelete: " << *dynamicVar << std::endl;  // Output: Undefined dangling pointer

    //Setelah melakukan delete, adalah praktik yang baik untuk mengatur pointer ke nullptr untuk menghindari penggunaan pointer yang tidak valid:
    dynamicVar = nullptr;  // Mengatur pointer ke nullptr
    //std::cout << "Nilai dari dynamicVar setelah diatur ke nullptr: " << *dynamicVar << std::endl;

    int arr[] = {1, 2, 3, 4, 5};
    int* ptr = arr;  // ptr menunjuk ke elemen pertama dari arr

    // ketika menggunakan nama array, itu secara otomatis dianggap sebagai pointer ke elemen pertama dari array.
    std::cout << "Elemen pertama: " << *ptr << std::endl;  // Output: 1
    // Meskipun pointer menunjuk ke elemen pertama, Anda dapat mengakses elemen lain dalam array dengan menggunakan aritmetika pointer. Misalnya, *(arr + 1) akan memberikan nilai dari elemen kedua (arr[1]).
    std::cout << "Elemen kedua: " << *(ptr + 1) << std::endl;  // Output: 2


    std::vector<int> numbers = {1, 2, 3, 4, 5};  // Vektor input
    std::vector<int> squared(numbers.size()); 
    printArrayVector(numbers);

    // Cara menggunakan lamba dengan transform
    /* [capture](parameters) -> return_type {
        // body of the lambda
        }*/ 

    /*Capture: Bagian [] adalah bagian capture, di mana Anda dapat menentukan variabel dari lingkup luar 
    yang ingin Anda gunakan di dalam lambda. Jika tidak ada variabel yang perlu di-capture, 
    Anda bisa meninggalkannya kosong seperti [].
    Parameters: Bagian (int x) adalah daftar parameter yang diterima oleh lambda. 
    Dalam contoh ini, lambda menerima satu parameter bertipe int yang dinamakan x.*/

    // menggunakan tambahan variabel dari lingkup luar
    int addValue = 10;
    std::transform(numbers.begin(),numbers.end(),squared.begin(),[addValue](int x){
        return x * x + addValue;  // Lambda function untuk menghitung kuadrat
    });
    printArrayVector(squared);

    // auto adalah sebuah keyword di C++ yang digunakan untuk mendeklarasikan variabel dengan tipe yang ditentukan secara otomatis oleh compiler berdasarkan nilai yang diinisialisasi
    // sekaligus membuat lambda function
    auto multiplyset = [addValue](int&x){
         x *= addValue;
    };
    printArrayVector(numbers);
    std::for_each(numbers.begin(),numbers.end(),multiplyset);
    printArrayVector(numbers);

    int arra[] = {1000000,2,3,4};
    for (int i= 0; i < sizeof(arra)/sizeof(arra[0]);i++) {
        std::cout << "Nilainya : " << arra[i] << std::endl;  
    }
    
    std::cout << "ukuran :" << sizeof(arra)/sizeof(arra[0]) << std::endl; 

    std::vector<int> array1 = {1, 2, 3};
    std::vector<int> array2 = {4, 5, 6};

    // Vektor untuk menyimpan hasil
    std::vector<int> result;

    // Menggunakan std::transform untuk menjumlahkan elemen dari dua vektor
    std::transform(array1.begin(), array1.end(), array2.begin(), std::back_inserter(result),
                   [](int a, int b) { return a + b; });

    // Mencetak hasil
    std::cout << "Hasil penggabungan: ";
    for (int value : result) {
        std::cout << value << " ";
    }
    std::cout << std::endl;

    std::vector<int> array3 = {4, 5, 6};
    std::vector<int> result2;

    std::transform(array1.begin(), array1.end(), array3.begin(), std::back_inserter(result2),
                   add);

    std::cout << "Hasil penggabungan 2: ";
    for (int value : result) {
        std::cout << value << " ";
    }
    std::cout << std::endl;                

    // Membuat filter function dengan fungsi copy_if
    std::vector<int> numbers2 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};

    // Vektor untuk menyimpan hasil filter
    std::vector<int> evenNumbers;
    std::vector<int> oddNumbers;

    // std::copy_if: Menyalin elemen yang memenuhi kondisi.
    std::copy_if(numbers2.begin(), numbers2.end(), std::back_inserter(evenNumbers),
                 [](int x) { return x % 2 == 0; });  // Lambda function untuk kondisi filter
                 
    // std::remove_copy_if: Menyalin elemen yang tidak memenuhi kondisi.             
    std::remove_copy_if(numbers2.begin(), numbers2.end(), std::back_inserter(oddNumbers),
                [](int x) { return x % 2 == 0; });  // Lambda function untuk kondisi filter


    std::cout << "Angka genap: ";
    for (int value : evenNumbers) {
        std::cout << value << " ";  // Output: 2 4 6 8 10
    }
    std::cout << std::endl;

    std::cout << "Angka ganjil: ";
    for (int value : oddNumbers) {
        std::cout << value << " ";  // Output: 2 4 6 8 10
    }
    std::cout << std::endl;
    return 0;
}