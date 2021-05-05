#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>


int main() {
	
	int min, max = 0;
	int index, temp;
	int num[3];
	
	

	for (int i = 0; i < 3; i++) {
		scanf("%d", &num[i]);
	}
	for (int i = 0; i < 3; i++) {
		min = 1000001;
		for (int j = i; j < 3; j++) {
			if (num[j] < min) {
				min = num[j]; index = j;
			}
		}
		temp = num[i];
		num[i] = num[index];
		num[index] = temp;
		printf("%d ", num[i]);

	}
		
	/*for (int i = 0; i < 3; i++) {
	}
	*/


	return 0;
}
	