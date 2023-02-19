# C13. 정렬 - 기출 문제 '안테나'
# 시간 초과 -> 괜히 어렵게 풂

import sys
input = sys.stdin.readline

# 모든 집까지의 거리의 총합이 최소가 되는 지점의 집 선택

n = int(input())
position = list(map(int, input().split()))

position.sort()
# 중간값에 위치하는 게 무조건 최소!
# 인덱스니까 - 1 (4번째는 인덱스 3이니까)
print(position[(n-1) // 2])



# -----------------------
# 시간 초과 풀이

# antenna_house = [] 
# for standard in position:
#     sum = 0
#     for i in range(n):
#         sum += abs(standard - position[i])
#     # standard에 위치한 안테나의 집 거리 총합 (위치, 합)
#     antenna_house.append([standard, sum]) 

# # 총합 작은 순으로 정렬, 동일할 경우 작은 집으로 정렬
# antenna_house.sort(key=lambda x: (x[1], x[0]))

# print(antenna_house[0][0])