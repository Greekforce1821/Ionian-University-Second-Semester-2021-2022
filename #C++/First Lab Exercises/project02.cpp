#include <iostream>
#include <iomanip>  
using namespace std;
 
int main()
{
	int y[5]={2018,2019,2020,2021,2022};
	int x[5]={157,3571,927,3675,56};

	for(int i=0;i<5;i++){
	    cout << setw(5) << y[i] << setw(6)  << x[i]<< endl;
    }
	return 0;
}
