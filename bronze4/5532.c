#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int up(int a, int b) {
	if (a % b != 0) return a / b + 1;
	else return a / b;
}

int main() {
	int l, a, b, c, d, x;
	
	scanf("%d", &l);
	scanf("%d", &a);
	scanf("%d", &b);
	scanf("%d", &c);
	scanf("%d", &d);

	
	x = up(a, c) > up(b, d) ? l - up(a, c) : l - up(b, d);
	printf("%d", x);


	return 0;
}
	