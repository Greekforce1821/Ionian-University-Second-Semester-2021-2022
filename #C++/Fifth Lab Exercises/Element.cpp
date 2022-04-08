#include "Element.h"
using namespace std;

Element::Element(){
}

Element::Element(int an, string n,string s,double am){
	a_num = an;
	name = n;
	symbol = s;
	a_mass = am;
}

int Element::get_a_num(){
	return a_num;
}
		
string Element::get_name(){
	return name;
}
		
string Element::get_symbol(){
	return symbol;
}
		
double Element::get_a_mass(){
	return a_mass;
}
