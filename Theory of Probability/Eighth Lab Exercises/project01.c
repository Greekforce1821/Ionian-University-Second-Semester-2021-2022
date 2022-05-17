#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>


int x;
int y;
int rw[1000][1000]={0,0};


int position1; 
int i; // first loop


int j; //second loop
int position2; 


int h = 0; // counter for Heads
int t = 0; // counter for Tails

int results_heads; //expected result for heads experiment
int results_tails; //expected result for tails experiment

int position_heads; //position for Heads
int position_tails; //position for Tails

int k; // third loop
int l; // fourth loop

double var;
double mn;


int sum_heads = 0; 
int sum_tails = 0; 
double sqdiff_heads = 0; 
double sqdiff_tails = 0; 

int main(){
	
	srand(time(NULL));
	
	x = rand()%1000+1;
	printf("The result of the random number x is: %d\n", x);
	
	y = rand()%1000+1;
	printf("The result of the random number y is): %d\n", y);
	
	for(i=0; i<=1000; i++){
		for(j=0; j<1000; j++){
			
			if(x>500 && y>500){
				position1 = x+1;
				position2 = y;
			}
			else if(x<500 && y<500){
				position1 = x-1;
				position2 = y;
			}
			else if(x<500 && y>500){
				position1 = x;
				posistion2 = y+1;
			}
			else if(x>500 && y<500){
				position1 = x;
				position2 = y-1;
			}
		}
		
		printf("%d\n", position1);
		printf("%d\n", position2);
	}
	
	printf("%d\n", position1);
	printf("%d\n", position2);
	
	FILE *fp;
	fp = fopen("walkers_eighth_lab_exercise.txt", "w");
	fprintf(fp, "%d\n", position1);
	fprintf(fp, "%d\n", position2);
	
	//for separate positions into separate files
	FILE *fp1;
	fp1 = fopen("walkers_eighth_lab_exercise_1.txt", "w");
	fprintf(fp1, "%d\n", position1);
	
	FILE *fp2;
	fp2 = fopen("walkers_eighth_lab_exercise_2.txt", "w");
	fprintf(fp2, "%d\n", position2);
	
	
	results_heads = rand()%100 +1;
	printf("The random heads result is: %d\n", results_heads);
			
	
	results_tails = rand()%100 +1;
	printf("The random tails result is: %d\n", results_tails);
	
	for(k=0; k<=1000; k++){
		for (l=0; l<=1000; l++){
			
			if (results_heads >70 && results_tails <30){
				position_heads = results_heads + 1;
				position_tails = results_tails;
				h++;
			}
			else if(results_heads <70 && results_tails >30){
				position_heads = results_heads;
				position_tails = results_tails + 1;
				t++;
			}
		}
		
		printf("%d\n", position_heads);
		printf("%d\n", position_tails);
		
		
		sum_heads = sum_heads + position_h;
		sqdiff_heads = sqdiff_heads + (position_heads - mn) * (position_heads - mn);
		
		
		sum_tails = sum_tails + position_t;
		sqdiff_tails = sqdiff_tails + (position_tails - mn) * (position_tails - mn);
		
		
		mn = (sum_h + sum_t)/1000;
		printf("%f\n", mn);
		
			
		var = (sqdiff_h + sqdiff_t)/1000;
		printf("%f\n", var);
		
	}
	
	return 0;
}
