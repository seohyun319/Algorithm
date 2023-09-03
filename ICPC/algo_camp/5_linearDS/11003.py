# platinum5-11003. 최솟값 찾기

import sys
from collections import deque
input = sys.stdin.readline

# 본인 포함 본인부터 본인 기준 L번째 왼쪽(Ai-L+1 ~ A)까지 중 최솟값 리스트 출력

n, l = map(int, input().split())
array = list(map(int, input().split()))

# 슬라이딩 윈도우로 L 범위만큼만 이동

q = deque()
for i in range(n):
    if q and i - l + 1 > q[0][0] : q.popleft() # 봐야 할 범위의 최소 인덱스보다 작은 인덱스가 남아있으면 버림
    while q and q[-1][1] > array[i]: # 큰 수 버리기
        q.pop()
    q.append((i, array[i]))
    print(q[0][1], end=' ')
