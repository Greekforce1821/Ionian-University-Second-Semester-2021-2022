#include <stdio.h>
int main() {
    int n, i;
    float num[10], sum = 0.0, avg;

    printf("Enter the numbers of elements: ");
    scanf("%d", &n);

    while (n > 10 || n < 1) {
        printf("Error! number should in range of (1 to 10).\n");
        printf("Enter the number again: ");
        scanf("%d", &n);
    }

    for (i = 0; i < n; ++i) {
        printf("%d. Enter number: ", i + 1);
        scanf("%f", &num[i]);
        sum += num[i];
    }

    avg = sum / n;
    printf("The Average Price of the Children Weight is = %.2f", avg);
    return 0;
}
