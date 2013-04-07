//http://projecteuler.net/problem=3
//Find largest prime factor of a composite number

//@ Heintze, Roland

#include<stdio.h>
#include<stdlib.h>

int main(int argc, char * argv[]) {
	if(argc!=2) {
		printf("Usage: ./sol3 n\nWhere n is a composite number.\n");
		return 0;
	}
	long n = atoi(argv[1]);
	int factor = 2, highestFactor = 1;
	printf("You entered: %ld\n",n);
	while(n > 1) {
		if(n % factor == 0) {
			highestFactor = factor;
			n = n/factor;
			while(n % factor == 0) n = n/factor;
		}
		factor++;
	}
	printf("Largest prime factor = %d\n", highestFactor);

	return 0;
}
