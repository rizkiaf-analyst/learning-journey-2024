#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

struct Booking {
    string roomtype;
    string startDate;
    string endDate;
};

int singleRooms = 2;
int doubleRooms = 5;

void checkRoomLeft(string roomtype){
    if (roomtype == "single") {
        cout << singleRooms << endl ;
    }
    else if(roomtype == "double") {
        cout << doubleRooms << endl ;
    }
}
bool checkAvailability(string roomtype){
    if (roomtype == "single") {
        return singleRooms > 0;
    }
    else if(roomtype == "double") {
        return doubleRooms > 0 ;
    }
    return false;
}
void bookRoom (string roomtype){
    if (roomtype == "single"){
        singleRooms--;
    }
    else if (roomtype == "double"){
        doubleRooms--;
    }
}
void processPayment(string customerID) {
    cout << "Payment already being process: " << customerID << endl;
}
string makeReservation(string customerID, string roomtype, string stardDate, string endDate, vector<string>& customer_list){
    if(checkAvailability(roomtype)) {
        bookRoom(roomtype);
        processPayment(customerID);
        customer_list.push_back(customerID);
        return "Reservation accepted";
    } else {
        return "Room already fully booked for customer : " + customerID;
    }
}

int main(){
    vector<string> customer_list;
    string cus1 = makeReservation("Rizki","single","2025-03-09","2025-03-11",customer_list);
    cout << cus1 << endl;
    string cus2 = makeReservation("Marine","single","2025-03-09","2025-03-11",customer_list);
    cout << cus2 << endl;
    string cus3 = makeReservation("HW","single","2025-03-09","2025-03-11",customer_list);
    cout << cus3 << endl;

    // Menampilkan daftar pelanggan yang menginap
    cout << "Daftar pelanggan yang menginap:" << endl;
    for (const string& customerID : customer_list) {
        cout << customerID << endl;
    }
    checkRoomLeft("single");
    checkRoomLeft("double");

    cout << sizeof(cus1) << endl;
    cout << sizeof(customer_list) << endl;
    for (const string& customerID : customer_list) {
        cout << sizeof(customerID) << endl;
    }
    return 0;
}