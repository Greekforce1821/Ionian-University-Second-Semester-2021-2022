#include <iostream>
#include <fstream>
#include <iomanip>
#include "Split.h"
#include "Element.h"
using namespace std;

int main(){
	int a_num;
	string name,symbol;
	double a_mass;
	string* l;
	Element el[200];
	ifstream fin;

	fin.open("elements_eng.txt");
	string line;
	getline(fin,line);
	int i = 0;
	while(getline(fin,line)){
		l = split(line,30,',');
		a_num = stoi(l[0]);
		name = l[1];
		symbol = l[2];
		a_mass = stod(l[3]);
		el[i] = Element(a_num,name,symbol,a_mass);
		i++;
	}
	fin.close();
	for(int j = 0; j<i; j++){
		if((el[j].get_a_mass() > 50.0) && (el[j].get_a_mass() < 100.0)){
			cout << left << setw(10) << el[j].get_name() << " " << setw(2) << el[j].get_symbol() << " " << el[j].get_a_mass() << endl;
		}
	}
	return 0;
}
