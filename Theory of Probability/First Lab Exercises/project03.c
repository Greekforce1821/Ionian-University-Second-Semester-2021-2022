#include <stdio.h>
#include <stdlib.h>

int main()
{

	for(int i=1; i<=10; i++)
	{
		printf("The Random Number is: %d \n", rand());
	}
	
	printf("The Max Value is : %d\n",	RAND_MAX);
    return 0;
}
