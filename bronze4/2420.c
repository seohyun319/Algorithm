#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <math.h>


int main() {
	long long n,m;
	
	scanf("%lld %lld", &n, &m);   
	printf("%lld", llabs(m - n));

	/*if (n<0 && m>0) printf("%d", m-n);
	else if (n>0 && m<0) printf("%d", n-m);
	else if (n < 0 && m < 0) printf("%d", -n - m);
	else if (n > 0 && m > 0 && n>m) printf("%d", n - m);
	else if (n > 0 && m > 0 && m > n) printf("%d", m - n);*/

	return 0;
}
	