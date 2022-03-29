#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(){
	
	srand(time(NULL));
	int i=0, result=0;
	
	int h = 0; 
	int t = 0; 
	
	for(i=1; i<=10; i++){
		result = rand()%2 +1;
		printf("The Selected Random integer number is: %d\n", result);
		
		if (result==1){
			h++;
		} else{
			t++;
		}
	}
	
	return 0;
}
