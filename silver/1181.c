#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

int compare(const void* a, const void* b) {
	if (*(int*)a > * (int*)b)
		return -1;
	else if (*(int*)a < *(int*)b)
		return 1;
	else
		return 0;
}

int main() {
	int num = 0;
	int n = 0;
	int* arr = (int*)malloc(sizeof(int) * num);
	scanf("%d", &n);
	while (n > 0) {
		arr[num] = n % 10;
		n = n / 10;
		num++;
	}

	qsort(arr, num, sizeof(int), compare);
	for (int i = 0; i < num; i++)
		printf("%d", arr[i]);

	return 0;
}