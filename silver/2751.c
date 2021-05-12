#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

int compare(const void* a, const void* b) {
	//return (*(int*)a) - (*(int*)b);
	if (*(int*)a > * (int*)b)
		return 1;
	else if (*(int*)a < *(int*)b)
		return -1;
	else
		return 0;
}


int main() {
	int num;
	scanf("%d", &num);
	int* arr = (int*)malloc(sizeof(int) * num);
	for (int i = 0; i < num; i++)
		scanf("%d", &arr[i]);
	qsort(arr, num, sizeof(int), compare);
	for (int i = 0; i < num; i++)
		printf("%d\n", arr[i]);
	free(arr);
	return 0;



}
