#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

typedef struct {
	int age;
	char name[101];
}people;

//int compare(const void* a, const void* b) {
//	if (*(int*)a > * (int*)b)
//		return 1;
//	else if (*(int*)a < *(int*)b)
//		return -1;
//	else
//		return 0;
//}

int compare(people *a, people *b) {
	if (a->age > b->age)
		return 1;
	else if (a->age < b->age)
		return -1;
	else
		return 0;
}

int main() {

	int num;
	scanf("%d", &num);

	people* arr = (people*)malloc(sizeof(people) * num);
	for (int i = 0; i < num; i++)
		scanf("%d %s", &arr[i].age, &arr[i].name);
	qsort(arr, num, sizeof(people), compare);
	for (int i = 0; i < num; i++)
		printf("%d %s\n", arr[i].age, arr[i].name);
	return 0;



}
