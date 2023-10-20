# silver3 - 2346. 풍선 터뜨리기
import sys 
from collections import deque
input = sys.stdin.readline

n = int(input())
nums = deque(enumerate(map(int, input().split())))

while nums:
    bomb = nums.popleft() # 터트린 풍선
    print(bomb[0] + 1, end=' ') # 인덱스 0부터 시작하니까 1 더해줌
    if bomb[1] > 0: # 쪽지에 적힌 수가 양수
        nums.rotate(-(bomb[1] - 1)) # popleft()로 이미 한 칸 간 효과
    else:
        nums.rotate(-bomb[1])