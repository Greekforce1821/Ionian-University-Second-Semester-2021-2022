#ifndef MYRANDOM_H
#define MYRANDOM_H
#include "MyRandom.h"
#endif
#include <string>
#include <iostream>
using namespace std;

class Q_Add {
	private:
	    static MyRandom mr;
		int a,b;
	public:
		Q_Add(int m);
		void print_quest() const;
		int get_Correct() const;
};
