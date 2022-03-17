#include <stdio.h>
#include <stdlib.h>
#include <time.h>

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
	
		printf("1 %d\n", c1);
		printf("2 %d\n", c2);
		printf("3 %d\n", c3);
		printf("4 %d\n", c4);
		printf("5 %d\n", c5);
		printf("6 %d\n", c6);
		
		FILE *fp;
		fp = fopen("txt", "w");
		
		fprintf(fp, "%d\n", c1);
		fprintf(fp, "%d\n", c2);
		fprintf(fp, "%d\n", c3);
		fprintf(fp, "%d\n", c4);
		fprintf(fp, "%d\n", c5);
		fprintf(fp, "%d\n", c6);
		
		fclose(fp);
	return 0;
}
