#include <iostream>
#include "Q_Add.h"

int main(){
	int score = 0, total = 0;
	int answ;
	
	while (score < 3){
		Q_Add q1(20);
		q1.print_quest();
		cin >> answ;
		if (answ == q1.get_Correct()){
			cout << "Σωστά !" << endl;
			score++;
		}
		else {
			cout << "Λάθος. Η σωστή απάντηση είναι: " << q1.get_Correct() << endl;
		}
		total++;
	}
	cout << "Ερωτήσεις : " << total << " Σωστές απαντήσεις : " << score << endl;
	return 0;
};
