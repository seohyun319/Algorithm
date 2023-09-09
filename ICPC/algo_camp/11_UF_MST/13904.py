# gold3-13904. 과제

import sys, heapq
input = sys.stdin.readline

# 과제 마감일 지켜야 점수 받을 수 있음.
# 얻을 수 있는 점수 최대값 

n = int(input())
day_score_list = [list(map(int, input().split())) for _ in range(n)] # 과제 마감일까지 남은 일수, 과제의 점수

day_score_list.sort() # 기한순 정렬
q = []
for day, score in day_score_list:
    heapq.heappush(q, score)
    if len(q) > day: # 기한보다 처리해야 하는 애가 많은 경우
        heapq.heappop(q) # 점수 제일 작은 애를 빼줌

print(sum(q)) # pop되지 않고 남아있는 애들: 각자 날짜에 순서대로 하면 됨
