# bronze3-6131. 완전 제곱수

import sys
input = sys.stdin.readline

# A의 제곱은 B의 제곱보다 N만큼 크다는 조건을 만족하는 A와 B 쌍의 개수

n = int(input())
squares = [0]*501
cnt = 0

for i in range(1, 501):
    squares[i] = i * i

for i in range(1, 501):
    for j in range(i, 501):
        if squares[j] - squares[i] == n:
            cnt += 1

print(cnt)
