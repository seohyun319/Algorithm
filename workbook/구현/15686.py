# gold4-15686. 치킨 배달

import sys
from itertools import combinations
input = sys.stdin.readline

# 폐업시키지 않을 치킨집을 최대 M개를 골랐을 때, 도시의 치킨 거리의 최솟값
# 치킨 거리: 집 근처에서 가장 가까운 치킨집까지의 거리

n, m = map(int, input().split()) # 도시 크기, 폐업 안 시킬 치킨집 최대 개수
graph = [[0] * (n + 1)]
for _ in range(n):
    graph.append([0] + list(map(int, input().split()))) # 0은 빈 칸, 1은 집, 2는 치킨집
houses = []
chicken_stores = []
chicken_distance_sum = []

# 집, 치킨집 좌표 리스트 만듦
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if graph[i][j] == 1:
            houses.append((i, j))
        if graph[i][j] == 2:
            chicken_stores.append((i, j))

chicken_candidates = list(combinations(chicken_stores, m))

for store in chicken_candidates:
    # 각 조합마다 집 기준 치킨 거리
    min_distance = 0
    for house_x, house_y in houses:
        temp = int(1e9)
        for chicken_x, chicken_y in store:
            nx, ny = house_x - chicken_x, house_y - chicken_y
            temp = min(temp, abs(nx) + abs(ny)) # 치킨거리
        min_distance += temp
    chicken_distance_sum.append(min_distance)

print(min(chicken_distance_sum))
