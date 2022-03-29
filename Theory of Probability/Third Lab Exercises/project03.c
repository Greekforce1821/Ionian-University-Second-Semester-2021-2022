#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(int argc, char** argv){
	
	#define N 10
	
	int i=0;
	double result;
	
	int c1;
	int c2;
	int c3;
	int c4;
	int c5;
	int c6;
	int c7;
	int c8;
	int c9;
	int c10;
		
	for(i=1; i<=N; i++){
		
		result = (double) rand()/RAND_MAX;
		printf("The doubled value is: %f\n", result);
		
		if (result>=0.0 && result <0.1){
			c1++;
		}
		else if (result>=0.1 && result<0.2){
			c2++;
		}
		else if (result>=0.2 && result<0.3){
			c3++;
		}
		else if (result>=0.3 && result<0.4){
			c4++;
		}
		else if (result>=0.4 && result<0.5){
			c5++;
		}
		else if (result>=0.5 && result<0.6){
			c6++;
		}
		else if (result>=0.6 && result<0.7){
			c7++;
		}
		else if (result>=0.7 && result<0.8){
			c8++;
		}
		else if (result>=0.8 && result<0.9){
			c9++;
		}
		else if (result>=0.9 && result<1.0){
			c10++;
		}
		
	}
	
	printf("%d\n", c1);
	printf("%d\n", c2);
	printf("%d\n", c3);
	printf("%d\n", c4);
	printf("%d\n", c5);
	printf("%d\n", c6);
	printf("%d\n", c7);
	printf("%d\n", c8);
	printf("%d\n", c9);
	printf("%d\n", c10);
	
	FILE *fp;
	fp = fopen("counters.txt", "w");
	
	fprintf(fp, "%d\n", c1);
	fprintf(fp, "%d\n", c2);
	fprintf(fp, "%d\n", c3);
	fprintf(fp, "%d\n", c4);
	fprintf(fp, "%d\n", c5);
	fprintf(fp, "%d\n", c6);
	fprintf(fp, "%d\n", c7);
	fprintf(fp, "%d\n", c8);
	fprintf(fp, "%d\n", c9);
	fprintf(fp, "%d\n", c10);
	
	fclose(fp);
	return 0;
}
