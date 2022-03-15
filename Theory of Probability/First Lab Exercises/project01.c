#include <stdio.h>
#include <stdlib.h>
#include <time.h>
int main()
{
    FILE *fp;
    int C1 = 0, C2 = 0, C3 = 0, C4 = 0, C5 = 0, C6 = 0;
    fp = fopen("dice.csv", "w+");
    fprintf(fp, "C1, C2, C3, C4, C5, C6\n");
    for(int j = 10; j <= 1000000; j = j * 10){
        for (int i = 0; i <= j; i++){
            srand(time(NULL)+i);
            switch((rand()%6)+1){
                case 1:
                    C1++;
                    break;
                case 2:
                    C2++;
                    break;
                case 3:
                    C3++;
                    break;
                case 4:
                    C4++;
                    break;
                case 5:
                    C5++;
                    break;
                case 6:
                    C6++;
                    break;
            }
        }
        fprintf(fp," %d, %d, %d, %d, %d, %d\n", C1, C2, C3, C4, C5, C6);
    }
    return 0;
}
