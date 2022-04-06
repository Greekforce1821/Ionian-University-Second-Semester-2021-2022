#include <iostream>
#include "Vehicle.h"

using namespace std;

Class Mcycle : public Vehicle {
              private:
                      int sidecar; // μεταβλητή για το αν το δίκυκλο έχει sidecar

              public:
                     Mcycle();
                     Mcycle(string owner, string number, int year);
                     void show(); // συνάρτηση για την εμφάνιση των στοιχείων του οχήματος
}; 
                