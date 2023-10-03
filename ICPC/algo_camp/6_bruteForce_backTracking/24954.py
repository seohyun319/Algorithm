# silver1-24954. 물약 구매

import sys
input = sys.stdin.readline
from itertools import permutations

# 물약을 구매하는 순서가 중요할 때, 물약을 가장 싸게 샀을 때의 비용
# 특정 물약을 구매하면 다른 물약의 가격이 할인됨
# 단, 물약의 가격이 0원이 되는 경우는 없음. 최대 할인가 적용해도 최소 1원은 지불해야 함

n = int(input()) # 물약의 종류
costs = [0] + list(map(int, input().split())) # 물약의 가격
potion_infos = [[] for _ in range(n+1)] 
for i in range(1, n+1):
    p = int(input()) # 물약의 종류
    for _ in range(p):
        potion_infos[i].append(list(map(int, input().split()))) # 물약의 정보 (물약 번호, 할인되는 가격)
minimum_total_price = sum(costs)

for potion_order_list in permutations(range(1, n+1), n):
    total_price = 0
    discount_prices = [0] * (n+1)
    for potion_num in potion_order_list:
        # 할인가 적용한 가격 (최소 1원 보장)
        total_price += max(costs[potion_num] - discount_prices[potion_num], 1)
        # 할인되는 물약 존재하면 가격 차감
        if potion_infos[potion_num]: 
            for num, discount_cost in potion_infos[potion_num]:
                discount_prices[num] += discount_cost
    minimum_total_price = min(total_price, minimum_total_price)

print(minimum_total_price)
