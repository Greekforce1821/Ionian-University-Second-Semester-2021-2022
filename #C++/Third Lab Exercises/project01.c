#include <iostream>
#include <string>
#include <iomanip> 
using namespace std;

class Student{
	private:
		static int count;
		string name;
		int am;
		
	public:
		Student(string n){
			count++;
			am = count;
			name = n;
		}
		void print_s() const{  
			cout << "Αριθμός Μητρώου : " << setfill('0') << setw(3) << am << " Όνομα : " << name << endl;
		}
};
int Student::count = 0;  
  
int main() {
    Student s1("Ιωάννης Παπατρέχας");
    Student s2("Ηλίας Παπαγεωργίου");
    Student s3("Τζοάννα Μαφιόζου");
    
    s1.print_s();
    s2.print_s();
    s3.print_s();
    return 0;
}
