# silver4-13305. 주유소

import sys
put = sys.stdin.readline

# 각 도시에 있는 주유소의 기름 가격과, 각 도시를 연결하는 도로의 길이를 입력으로 받아 제일 왼쪽 도시에서 제일 오른쪽 도시로 이동하는 최소의 비용을 계산

n = int(put()) # 도시 개수
length = list(map(int, put().split())) # 도로의 길이
price = list(map(int, put().split())) # 주유소의 리터당 가격

# (i-1)번째에서 i번째 도시로 가는 거리에 소모되는 기름은 
# 1 ~ (i-1)번째 주유소 중 가장 가격이 싼 도시의 주유소 고르면 됨
sum = 0
min_price = price[0]
for i in range(n-1):
    if min_price > price[i]:
        min_price = price[i]
    sum += min_price * length[i]  
print(sum)