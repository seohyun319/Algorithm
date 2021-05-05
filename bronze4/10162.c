#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>


int main() {
	/*
	int min, max = 0;*/
	int t;
	//int num[3];
	
	scanf("%d", &t);   

	if (t%10==0) printf("%d %d %d", t/300, (t%300)/60, ((t%300)%60)/10);
	else printf("%d", -1);

	return 0;
	//t - (t / 300) * 300 - ((t - (t / 300) * 300) / 60) * 60) / 10
}
	