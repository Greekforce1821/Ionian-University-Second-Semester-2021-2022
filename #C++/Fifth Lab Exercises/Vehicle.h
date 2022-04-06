#include <iostream>

using namespace std;

Class Vehicle{
              private:
                      int year; // έτος κατασκευή
                      string number; // πινακίδα κυκλοφορίας
                      string owner; // κάτοχος ΙΧ
              public:
                     Vehicle();
                     Vehicle(string owner, string number, int year);
                     void set_owner(string o); // συνάρτηση για την αλλαγή του ιδιοκτήτη
                     void show(); // συνάρτηση για την εμφάνιση των στοιχείων του οχήματος
}; 
                