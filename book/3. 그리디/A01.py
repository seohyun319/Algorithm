# C11. GREEDY - 기출 문제 '모험가 길드'

import sys
input = sys.stdin.readline

# 모험가 N명, 공포도 X인 모험가는 반드시 X명 이상으로 구성된 모험가 그룹에 참여해야
# 모험가 몇몇은 마을에 남아있어도 됨.
# 여행 떠날 수 있는 모험가 그룹 수 최댓값 구하기

n = int(input())
fears = list(map(int, input().split()))

# 마을에 있어도 되는 사람의 수 제한 없음. 공포도가 큰 사람은 안 가도 되는 사람으로 빼는 방향으로...

fears.sort()

group = 0
# 공포도가 현재 그룹 사람 수로 커버 가능하면 포함하기
for i in range(1, n+1):
    # 1번째 1, 1+2번째 2, 1+2+3번째가 3이면 그룹 하나씩 만들어질 수 있음.
    sum_fear = int(((i)*(i+1))/2)    
    if sum_fear <= n:
        if fears[sum_fear - 1] == i:    
            group += 1
print(group)



# 다른 풀이
# for fear in fears:    
#     people += 1 # 이번 사람 카운팅
#     if fear <= people:
#         group += 1
#         people = 0 # 초기화
# print(group)
