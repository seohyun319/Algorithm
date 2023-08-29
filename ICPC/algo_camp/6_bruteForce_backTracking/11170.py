# bronze1-11170. 0의 개수

import sys
input = sys.stdin.readline

# N부터 M까지의 수들에 적힌 0들을 세기

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    cnt = 0
    for i in range(n, m + 1):
        for x in str(i):
            if x == "0":
                cnt += 1
    print(cnt)