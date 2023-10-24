# silver4 - 11047. 동전 0
import sys
input = sys.stdin.readline

coins = []
num = 0 # 필요한 동전 개수
answer = 0 # 필요한 동전 개수 총합
n, k = map(int, input().split())
for _ in range(n):
    coins.append(int(input()))

# for문 인덱스 -1로 돌리면서 하는 게 더 빠름!!
coins.sort(reverse=True)
for coin in coins:
    # if coin < k:로 해서 틀림 -> 같은 경우도 가능하다!
    if coin <= k:
        num = k // coin
        k -= (coin * num)
        answer += num

print(answer)