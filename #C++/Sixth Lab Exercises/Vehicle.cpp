#include <iostream>
#include "Vehicle.h"
using namespace std;

Vehicle::Vehicle(){
   
}

Vehicle::Vehicle(string o, string n, int y){

    owner = o;
    number = n;
    year = y;
    

}

void Vehicle::set_owner(string o){

    owner = o;

}

void Vehicle::show(){

    cout << "Αριθμός κυκλοφορίας: " << number << "-" << "Ιδιοκτήτης: " owner << "-" << "Έτος κατασκευής:" << year << endl;
}