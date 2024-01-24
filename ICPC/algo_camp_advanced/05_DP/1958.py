# gold3-1958. LCS 3

import sys
input = sys.stdin.readline

# 문자열 3개의 LCS 길이 출력

first = list(input().rstrip())
second = list(input().rstrip())
third = list(input().rstrip())
matrix = [[[0 for _ in range(len(third) + 1)] for _ in range(len(second) + 1)] for _ in range(len(first) + 1)]

for i in range(1, len(first) + 1):
    for j in range(1, len(second) + 1):
        for k in range(1, len(third) + 1):
            if first[i-1] == second[j-1] == third[k-1]:
                matrix[i][j][k] = matrix[i-1][j-1][k-1] + 1
            else: 
                matrix[i][j][k] = max(matrix[i-1][j][k], matrix[i][j-1][k], matrix[i][j][k-1])

print(matrix[i][j][k])