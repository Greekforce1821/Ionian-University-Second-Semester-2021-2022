#include "Q_Add.h"

Q_Add::Q_Add(int m){
	a = mr.get_number(m); 
	b = mr.get_number(m);
};

void Q_Add::print_quest(){
	cout << a << " + " << b << " = ";
};

int Q_Add::get_Correct(){
	return a+b;
};
MyRandom Q_Add::mr;
