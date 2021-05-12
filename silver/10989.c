#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

int main() {
	int num, temp;
	scanf("%d", &num);
	int arr[10001] = { 0 };

	for (int i = 0; i < num; i++) {
		scanf("%d", &temp);
		arr[temp]++;
	}
	for (int i = 0; i < 10001; i++)
		if (arr[i] >= 1) {
			for (int j = 0; j < arr[i]; j++) printf("%d\n", i);
		}
	return 0;


}
