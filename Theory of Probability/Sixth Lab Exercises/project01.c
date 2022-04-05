#include <stdio.h>
#include <stdlib.h>
#include <math.h>

double mean(double val[10], int n){
	
	double result;
	int i;
	int sum = 0;

	for(i=0; i<=10; i++){
		sum = sum + val[i];
	}
	
	result = sum/n;
	return result;
	
}

double variance(double val[10], int n){
	
	double s;
	int i;
	int sum = 0;
	
	double m;
	double sqdiff = 0;
	
	for (i=0; i<=10; i++){
		sum = sum + val[i];
		m = mean(val, 10);
		
		sqdiff = sqdiff + (val[i] - m) * (val[i] - m);
	}
	
	
	s = sqdiff/n;
	return s;
}

double stddev(double val[10], int n){
	
	double s;
	
	s = variance(val, 10);
	double sdv = sqrt(s);
	return sdv;
	
}

int main({
	
	int i;
	double val[10];
	double result;
	int n = 10;
	
	
	double m; 
	double v; 
	double sd; 
	
	for (i=0; i<=10; i++){
		val[i] = rand();
	}
	
	m = mean(val, 10);
	printf("%f\n", m);
	
	v = variance(val, 10);
	printf("%f\n", v);
	
	sd = stddev(val, 10);
	printf("%f\n", sd);
	
	return 0;
}

