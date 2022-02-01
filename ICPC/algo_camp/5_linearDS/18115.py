# silver3-18115. 카드 놓기

import sys
from collections import deque
put = sys.stdin.readline

# 카드 내려놓으며 기술 사용
# 1. 제일 위의 카드 1장을 바닥에 내려놓는다.
# 2. 위에서 두 번째 카드를 바닥에 내려놓는다. 카드가 2장 이상일 때만 쓸 수 있다.
# 3. 제일 밑에 있는 카드를 바닥에 내려놓는다. 카드가 2장 이상일 때만 쓸 수 있다.
# 다 내려놓으니 위부터 순서대로 1, 2, .. N
# 기술 1, 2, 3 중 하나 사용할 때 처음 카드 상태는?

n = int(put()) 
a = deque(map(int, put().split())) # 사용한 기술의 번호 나열한 수열 a

card = 0
origin = deque() # 처음 카드 상태
for i in range(1, n+1):
  card = a.pop() # a의 최신순으로 보기 위해 pop해서 담음
  if card == 1:
    origin.appendleft(i)
  if card == 2:
    # 처음 거 빼고 이번 차례 넣어주고 다시 위에 넣으면 됨
    x = origin.popleft()
    origin.appendleft(i)
    origin.appendleft(x)
  if card == 3:
    origin.append(i)

for x in origin:
  print(x, end=' ')
