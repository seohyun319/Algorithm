# gold4-19598. 최소 회의실 개수

import sys, heapq
input = sys.stdin.readline

# 회의를 모두 진행할 수 있는 최소 회의실 개수를 구하라

n = int(input())
meetings = [list(map(int, input().split())) for _ in range(n)]
rooms = []
cnt = 0

meetings.sort() # 시작 시간 기준 정렬

for start, end in meetings:
    # 이번 거의 시작 시간이 전 거의 끝나는 시간보다 빠르면 (들어갈 수 없으니 새 방 만듦)
    if not rooms or start < rooms[0]: 
        cnt += 1
        heapq.heappush(rooms, end)
    else:
        heapq.heappop(rooms)
        heapq.heappush(rooms, end)

print(cnt)
