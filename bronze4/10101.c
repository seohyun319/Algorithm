#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>


int main() {
	int a, b, c;
	
	scanf("%d", &a);
	scanf("%d", &b);
	scanf("%d", &c);

	if (a == 60 && b == 60 && c==60) printf("Equilateral");
	else if (a + b + c != 180) printf("Error");
	else if (a == b || b == c || a == c) printf("Isosceles");
	else if (a != b && b != c && a != c) printf("Scalene");


	return 0;
}
	