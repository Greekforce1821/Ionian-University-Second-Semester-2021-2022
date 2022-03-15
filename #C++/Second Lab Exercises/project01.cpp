#include <iostream>

using namespace std;

void p_line();
void p_line(char c);
void p_line(char c, int num);
void p_line(char c1,char c2, int num);

int main(){

	cout << "p_line()" << endl;
	p_line();
	cout <<  "p_line(\'*\')" << endl;
	p_line('*');
	cout << "p_line(\'#\',30)" << endl;
	p_line('#',30);
	cout <<  "p_line(\'-\',\'+\',20)" << endl;
	p_line('-','+',20);
	return 0;
}

void p_line(){
	for(int i=0;i<15;i++){
		cout << '-';
	}
	cout << endl;
}

void p_line(char c){
	for(int i=0;i<15;i++){
		cout << c;
	}
	cout << endl;
}

void p_line(char c, int num){
	for(int i=0;i<num;i++){
		cout << c;
	}
	cout << endl;
}

void p_line(char c1,char c2, int num){
	for(int i=0;i<num;i++){
		cout << c1 << c2 << c1;
	}
	cout << endl;
}
