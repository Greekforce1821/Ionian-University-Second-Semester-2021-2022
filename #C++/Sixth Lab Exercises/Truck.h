#include <iostream>
#include "Vehicle.h"

using namespace std;

Class Truck : public Vehicle {
              private:
                      int axis; // μεταβλητή για τον αριθμό τον αξόνων

              public:
                     Truck();
                     Truck(string owner, string number, int year);
                     void show(); // συνάρτηση για την εμφάνιση των στοιχείων του οχήματος
}; 
                