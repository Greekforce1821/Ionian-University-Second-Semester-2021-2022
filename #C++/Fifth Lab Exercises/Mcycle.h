#include <iostream>

using namespace std;

Class Mcycle{
              private:
                      int sidecar; // μεταβλητή για το αν το δίκυκλο έχει sidecar

              public:
                     Mcycle();
                     Mcycle(string owner, string number, int year);
                     void set_owner(string o); // συνάρτηση για την αλλαγή του ιδιοκτήτη
                     void show(); // συνάρτηση για την εμφάνιση των στοιχείων του οχήματος
}; 
                