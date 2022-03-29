#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(){
	
	int prob;
	int i=0;
	
	// int h, t;
	
	for(i=1; i<=100; i++){
		prob = rand()%10 + 1;
		if (prob>8){
			printf ("A \n"); // h++;
		} else{
			printf("B \n"); //t++;
		}
	}
	
	return 0;
}
