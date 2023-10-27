# gold5 - 11000. 강의실 배정
import sys, heapq

input = sys.stdin.readline

n = int(input())
classes = [list(map(int, input().split())) for _ in range(n)]

classes.sort()
rooms = []
heapq.heappush(rooms, classes[0][1])
for i in range(1, n):  # 맨 처음 거는 이미 넣음
    # 다음 시작시간이 rooms의 끝나는 시간과 같거나 클 때 (그 강의실에 배정 가능)
    if classes[i][0] >= rooms[0]:
        heapq.heappop(rooms)
        heapq.heappush(rooms, classes[i][1])
    else:  # 새 강의실 배정해야 하는 상황
        heapq.heappush(rooms, classes[i][1])

print(len(rooms))


"""
# 시간 초과
classes.sort(key=lambda x:x[1])
rooms = []
rooms.append(classes[0][1])
for i in range(1, n): # 맨 처음 거는 이미 넣음
    # 다음 시작시간이 rooms의 끝나는 시간과 같거나 클 때 (그 강의실에 배정 가능)    
    if classes[i][0] >= rooms[0]:
        # heapq의 경우 삽입시 알아서 정렬해줘서 시간 훨씬 빠름. 
        # rooms.sort() 정렬 필요.. (근데 시간초과 남)
        rooms.pop(0)
        rooms.append(classes[i][1])
    else: # 새 강의실 배정해야 하는 상황
        rooms.append(classes[i][1])

print(len(rooms))
"""
