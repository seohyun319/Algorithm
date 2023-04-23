# silver2-11501. 주식

import sys
from collections import deque
input = sys.stdin.readline

# 하루에 주식 하나를 사거나, 원하는 만큼 팔거나, 그냥 두거나
# 최대 이익 구하기
# 관심사: 최대 가격 가진 날. 그게 오늘보다 이후여야 함. 
# 현재 일수 포함 이후의 최대 가격 리스트 => 지금까지의 최대값

# 틀림 -> 반례때문에 i > day_and_price[0][0] 들어간 if문 추가함.
# 해당 if문에서 인덱스가 이미 지난 케이스를 while문 돌리면서 popleft 해줬더니 시간초과 -> 순서 맨 위로 바꿈
# 근데도 popleft가 일회성이라 원하는 인덱스까지 못 옴
# 그냥 실제 봐야 하는 중요한 정보인 최대값 배열을 만듦. 이때, 제일 최대값 -> 걔보다는 작지만 걔 다음에 오는 차선 최대값 이런 순으로 넣음. 

# 반례: 7 6 9 1 6. 9에서 다 팔고 마지막 6에서 팔아야 하는데 
# 최대값인 9(2번 인덱스_에서 팔면 day_and_price에 [0, 7] [1, 6], [4, 6]가 남아있음. 
# 판 시점 다음인 3번 인덱스 차례에서는 현재 인덱스가 최대값의 인덱스보다 커서 팔지도 사지도 못함

t = int(input())
for _ in range(t):
    n = int(input())
    prices = list(map(int, input().split()))
    profit, bought_number = 0, 0 #  이익, 구매한 주식 개수
    day_and_price = []
    max_price_list = []

    # 인덱스와 가격 담은 day_and_price 배열 만들어줌
    for idx, price in enumerate(prices):
        day_and_price.append([idx, price])
    day_and_price.sort(key=lambda x:-x[1]) # 가격 큰 순서로 정렬 -> 맨 앞이 최대값 
    
    # 반례) 최대값이긴 한데 이미 인덱스 지남
    # 인덱스 순서대로 담은 최대값 리스트 (최대값이 중간에 오는 경우 커버용)    
    max_price_list.append(day_and_price[0]) # 첫번째는 무조건 최대값
    max_price_idx = day_and_price[0][0]
    for idx in range(1, n):
        if day_and_price[idx][0] > max_price_idx:
            max_price_list.append(day_and_price[idx])
            max_price_idx = day_and_price[idx][0]
    max_price_list = deque(max_price_list) # popleft 위해 덱으로 바꿔줌
    
    for i in range(n):
        if i < max_price_list[0][0]: # 현재 인덱스가 최대값의 인덱스보다 작으면 최대값이 이후에 오니까 삼
            profit -= prices[i]
            bought_number += 1
        if i == max_price_list[0][0]: # 현재가 최대값이니까 팖
            profit += max_price_list[0][1] * bought_number # 최대값 * 샀던 주식 수
            bought_number = 0 
            max_price_list.popleft()
            
    print(profit)