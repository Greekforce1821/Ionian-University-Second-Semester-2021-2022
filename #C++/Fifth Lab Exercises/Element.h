#include <string>
using namespace std;


class Element{
	private:
		int a_num;
		string name;
		string symbol;
		double a_mass;
	public:
		Element();
		Element(int an, string n,string s,double am);
		int get_a_num();
		string get_name();
		string get_symbol();
		double get_a_mass();
};
