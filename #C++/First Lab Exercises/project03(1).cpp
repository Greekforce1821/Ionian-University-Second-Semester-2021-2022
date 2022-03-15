#include <iostream>
#include <iomanip>

using namespace std;

int main(){
    
    double eur_dolar = 1.144;
    double eur_yen = 131.541;
    double eur_chf = 1.053;
    double eur_pound = 0.842;
    double eur;

    cout << "Type a specific amount: ";
    cin >> eur;
    
    cout << "The " << eur << " in:\n Dolar is: "<< setprecision(3) << eur_dolar*eur <<"\n Yen is: "<< setprecision(3) << eur_yen*eur <<"\n CHF is: "<< setprecision(3) << eur_chf*eur <<"\n British Pound is: " << setprecision(3) << eur_pound*eur << endl;

    return 0;
}
