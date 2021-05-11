#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>


int main() {
	int a, b, c, d;

	scanf("%d %d %d", &a, &b, &c);
	scanf("%d", &d);
	if (d >= 3600) {
		a = a + d / 3600;
		b = b + (d % 3600)/ 60;
		c = c + d % 60;
	}
	else /*if (d >= 60)*/ {
		//h = h + (m + t / 60) / 60;
		b = b + d / 60;
		c = c + d % 60; 
	}/*
	else if (c + d >=60) {
		b = b + (c + d) / 60;
		c = (c + d)%60;
	}*/
		

	if (a >= 24) a = a %24;
	if (b >= 60) {
		a = a + b / 60;
		b = b % 60;
	}
	if (c >= 60) {
		b = b + c / 60;
		c = c % 60;
	}
	printf("%d %d %d", a, b, c);

	//if (t >= 3600) {
	//	if (h + t / 3600 >=24) printf("%d %d %d", h + t / 3600 - 24, m + t % 3600 + t / 60, s + t % 60);
	//	else if (m + t % 3600 + t / 60 >=60) printf("%d %d %d", h + t / 3600, m + t % 3600 + t / 60 -60, s + t % 60);
	//}
	//else if (t >= 60) {
	//	if ()
	//	if (m + t / 60 >=60) printf("%d %d %d", h + (m + t / 60)/60, m + t / 60 -60, s + t % 60);
	//}




	return 0;
}
