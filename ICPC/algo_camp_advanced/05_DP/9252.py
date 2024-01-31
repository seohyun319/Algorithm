# gold4-9252. LCS 2

import sys
input = sys.stdin.readline

# 문자열 2개의 LCS(Longest Common Subsequence, 최장 공통 부분 수열) 길이 출력

first = list(input().rstrip())
second = list(input().rstrip())
matrix = [['' for _ in range(len(second) + 1)] for _ in range(len(first) + 1)]

for i in range(1, len(first) + 1):
    for j in range(1, len(second) + 1):
        if first[i-1] == second[j-1]:            
            matrix[i][j] = matrix[i-1][j-1] + first[i-1]
        else:
            if len(matrix[i-1][j]) > len(matrix[i][j-1]):
                matrix[i][j] += matrix[i-1][j]
            else:
                matrix[i][j] += matrix[i][j-1]

print(len(matrix[i][j]))
print(matrix[i][j])