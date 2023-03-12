# silver4-11582. 치킨 TOP N

import sys
input = sys.stdin.readline

n = int(input()) # 치킨집 개수 (2의 거듭제곱)
taste_nums = list(map(int, input().split())) # 치킨집 맛의 수치
k = int(input()) # 정렬 진행중인 회원의 수 (2의 거듭제곱)

# n, k 둘다 2의 거듭제곱이라 n을 k로 나눈 몫만큼 숫자 자름. 

for i in range(n // k, n + 1, n // k):
    print(*sorted(taste_nums[i - (n//k) : i]), end=' ')
