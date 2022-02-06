# silver5-7568. 덩치

import sys
put = sys.stdin.readline

# 덩치 등수 계산
# 키, 몸무게 둘 다 커야 덩치가 크다고 할 수 있음
# 키, 몸무게 둘 중 하나가 크고 하나가 작으면 덩치 등수 동일하다고 침

n = int(put())
info = [list(map(int, put().split())) for _ in range(n)]

for i in range(n): # 나
  cnt = 1 # 등수는 1부터 시작
  for j in range(n): #남
    # 남이 나보다 키랑 몸무게 둘 다 크면 1 더해줌 
    if info[j][0] > info[i][0] and info[j][1] > info[i][1]:
      cnt += 1
  print(cnt, end=' ')


