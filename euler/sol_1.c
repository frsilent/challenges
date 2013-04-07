//http://projecteuler.net/problem=1
//Sum of multiples of 3 and 5 below 1000

//@ Heintze, Roland

#include<stdio.h>
#include<stdlib.h>

int main(int argc, char * argv[]) {
	int final = 0, i=0;
	for(i=0;i<1000;i++) {
		if((i%3==0)||(i%5==0)) final+=i;
	}
	printf("The final sum is: %d\n",final);

	return 0;
}
