//http://projecteuler.net/problem=4
//Find the larget palindrome made from the product of two 3-digit numbers

//@ Heintze, Roland

#include<stdio.h>
#include<stdlib.h>
#include<stdbool.h>

//function prototypes
bool palin(int n);

int main(int argc, char * argv[]) {
	int a, b;

	return 0;
}

bool palin(int n) {
	int reverse = 0; int temp = n;
	while(temp != 0) {
		reverse *=10;
		reverse += temp % 10;
		temp /= 10;
	}
	return (n == reverse);
}
