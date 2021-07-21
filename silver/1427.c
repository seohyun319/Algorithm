#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <string.h>


int compare(const void* a, const void* b) {
	int lenA = strlen(a);
	int lenB = strlen(b);
	if (lenA == lenB) {
		return strcmp((char*)a, (char*)b);
	}
	else if (lenA > lenB) {
		return 1;
	}
	else {
		return -1;
	}
}


int main() {
	int num;
	scanf("%d", &num);
	char word[num][51];
	
	for (int i = 0; i < num; i++)
		scanf("%s", &word[i]);
	qsort(word, num, sizeof(word[0]), compare);
	for (int i = 0; i < num; i++) {
		if (strcmp(word[i], word[i + 1]) == 0) {
			continue;
		} else {
			printf("%s\n", word[i]);
		}
	}	
	return 0;
}








