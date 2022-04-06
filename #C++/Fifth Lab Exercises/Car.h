#include <iostream>

using namespace std;

Class Car{
              private:
                      int year; // έτος κατασκευής
              protected:
                       string number; // πινακίδα κυκλοφορίας
                       string owner; // κάτοχος ΙΧ
              public:
                     Car();
                     Car(string owner, string number, int year);
                     void set_owner(string o); // συνάρτηση για την αλλαγή του ιδιοκτήτη
                     void show(); // συνάρτηση για την εμφάνιση των στοιχείων του οχήματος
}; 
                