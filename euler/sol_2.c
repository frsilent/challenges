//http://projecteuler.net/problem=2
//Sum of even terms in the Fibonacci sequence < Fibo[n]=4 million

//@ Heintze, Roland

//function prototypes
long recursiveSolve();
long iterativeSolve();

#include<stdio.h>
#include<stdlib.h>
#define MAX 4000000 // 4 million

int main(int argc, char *argv[]) {
	long rSolution, iSolution;
	rSolution = recursiveSolve();
	iSolution = iterativeSolve();

	printf("The result of the recursive algorithm is: %ld\n", rSolution);
	printf("The result of the iterative algorithm is: %ld\n", iSolution);

	return 0;
}

long recursiveSolve() {
	long sum = 0; int i, newFibo;
	i = 1;
	while(i++) {
		newFibo = fibo(i);
		if(newFibo >= MAX) break;
		else if(newFibo % 2 ==0) sum += newFibo;
	}

	return sum;
}
long iterativeSolve() {
	long sum = 0;
	int x = 1, y = 1;
	do {
		if( x % 2 == 0) sum += x;
		x += y; y = x - y;
	} while (x < MAX);

	return sum;
}

//recursive fibonacci
int fibo(int n) {
	if(n==0||n==1) return 1; //stop condition
	else return fibo(n-1)+fibo(n-2);
}
