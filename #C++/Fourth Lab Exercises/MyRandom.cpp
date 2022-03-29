#include <cstdlib> 
#include <ctime>
#include "MyRandom.h"

MyRandom::MyRandom(){
	srand(time(0));
}

int MyRandom::get_number(int m){
	return (rand()%m) + 1;
}
