#include <iostream>

using namespace std;

Class Truck{
              private:
                      int axis; // μεταβλητή για τον αριθμό τον αξόνων

              public:
                     Truck();
                     Truck(string owner, string number, int year);
                     void show(); // συνάρτηση για την εμφάνιση των στοιχείων του οχήματος
}; 
                