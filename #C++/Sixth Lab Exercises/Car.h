#include <iostream>
#include "Vehicle.h"

using namespace std;

Class Car : public Vehicle {
              private:
                      int doors; // μεταβλητή για τον αριθμό θυρών

              public:
                     Car();
                     Car(string owner, string number, int year);
                     void show(); // συνάρτηση για την εμφάνιση των στοιχείων του οχήματος
}; 
                