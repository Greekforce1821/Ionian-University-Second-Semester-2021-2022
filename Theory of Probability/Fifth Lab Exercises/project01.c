#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(){
	srand(time(NULL));
	
	
	int i;
	int j;
	
	int counter;
	int s = 0;
	int a;
	
	int r;
	
	for (j=0; j<=100; j++){
		counter = 0; 
		for(i=0; i<=10; i++){
			r = rand()%2;
			printf("%d\n", r);
			a = 0;
			if (a == 0){
				if (i <= 3){
					if (r == 1){
						counter++;
					}
					else{
						a = 1;
					}
				}
			}
		}
		if (counter == 3){
			s++;
		}
		printf("\n");
	}
	
	printf("How many times does the dice got correct? %d\n", s);
	
	return 0;
