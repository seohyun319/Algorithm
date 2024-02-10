# silver4-11047. 동전 0

import sys
input = sys.stdin.readline

# K원을 만드는데 필요한 동전 개수의 최솟값

n, k = map(int, input().split())
worth = [int(input()) for _ in range(n)]
coin_cnt = 0

worth.sort(reverse=True)
for money in worth:
    if k >= money:
        coin_amount = k // money         
        k -= coin_amount * money
        coin_cnt += coin_amount

print(coin_cnt)