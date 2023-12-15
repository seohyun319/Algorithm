# silver1 - 1697. 숨바꼭질
import sys

input = sys.stdin.readline
from collections import deque

n, k = map(int, input().split())  # 수빈이의 위치, 동생의 위치
max = 100000
array = [0] * (max + 1)


def bfs():
    q = deque()
    q.append(n)
    while q:
        x = q.popleft()
        if x == k:  # 동생 찾음
            print(array[x])
            break
        for nx in [x + 1, x - 1, x * 2]:
            if 0 <= nx <= max and not array[nx]:
                array[nx] = array[x] + 1
                q.append(nx)


bfs()
