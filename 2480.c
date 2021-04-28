#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>


int main() {
	
	//int a, b, c;
	int dice[3], num;
	int count=0;
	int max = 0;
	
	
	/*scanf("%d %d %d", &a, &b, &c);

	if (a == b && b==c && a==c) {
		printf("%d", 10000 + a * 1000);
	}
	else if (a == b || a == c ) {
		printf("%d", 1000 + a * 100);
	}
	else if (b == c) {
		printf("%d", 1000 + b * 100);
	}
	else {
		if (a>b && a>c) printf("%d", a * 100);
		else if (a < b && c < b) printf("%d", b * 100);
		else printf("%d", c * 100);
	}*/


	scanf("%d ", &dice[0]);
	for (int i = 1; i < 3; i++) {
		scanf("%d", &dice[i]);
		if (dice[i-1] == dice[i]) {
			num = dice[i];
			count++;
		}
	}
	/*if (dice[0] == dice[2]) {
		num = dice[2];
		count++;
	}*/
	if (count == 2) printf("%d", 10000 + num * 1000);
	else if (count == 1) printf("%d", 1000 + num * 100);
	else if (dice[0] == dice[2]) {
		num = dice[2];
		printf("%d", 1000 + num * 100);
	}
	else {
		for (int i = 0; i < 3; i++) {
			if (dice[i] > max) max = dice[i];
		}
		printf("%d", max * 100);
	}
	return 0;
}
	