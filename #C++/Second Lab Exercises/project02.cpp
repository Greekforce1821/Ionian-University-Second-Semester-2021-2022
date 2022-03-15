include <iostream>

using namespace std;

struct Time {
	int hour;
	int min;
	int sec;
};

Time input_t(){
	Time t;
	cout << "Ώρα : ";
	cin >> t.hour;
	cout << "Λεπτά : ";
	cin >> t.min;
	cout << "Δευτερόλεπτα : ";
	cin >> t.sec;
	return t;
}

int time2sec(Time t){
	return (((t.hour*60)+t.min)*60)+t.sec;
}

Time sec2time(int s){
	Time t;
	t.hour = s / 3600;
	t.min = (s % 3600) / 60;
	t.sec = (s % 3600) % 60;
	return t;
}

Time interval(Time t1, Time t2){
	int s1 = time2sec(t1);
	int s2 = time2sec(t2);
	int s21 = s2 - s1;
	Time inter = sec2time(s21);
	
	return inter;
}

int main(){
	Time start,end,duration;
	
	cout << "Έναρξη" << endl;
	start = input_t();
	cout << "Τερματισμός" << endl;
	end = input_t();
	duration = interval(start,end);
	cout << "Διάρκεια = " <<  duration.hour << "ώρες " << duration.min << "λεπτά " << duration.sec << "δευτερόλεπτα" << endl;
	
	return 0;
}
