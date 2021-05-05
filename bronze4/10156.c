#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>


int main() {
	
	int min, max = 0;
	int k, n, m;
	int num[3];
	
	scanf("%d %d %d", &k, &n, &m);
	if (k * n - m <0) printf("%d", 0);
	else printf("%d", k*n-m);

	return 0;
}
	