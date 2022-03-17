#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>

int main(){
	
	srand(time(NULL));
	int i = 0; 
	int result = 0;
	int c1 = 0;
	int c2 = 0;
	int c3 = 0;
	int c4 = 0;
	int c5 = 0;
	int c6 = 0;
	
	for(i=1; i<=10; i++)
  {
		result = rand()%6 +1;
		printf("The Random Value of the Number is: %d\n", result);
		
		if (result==1){
			c1++;
		} else if (result == 2){
			c2++;
		} else if (result == 3){
			c3++;
		} else if (result == 4){
			c4++;
		} else if (result == 5){
			c5++;
		} else{
			c6++;
		}
	}
  
	return 0;
}
