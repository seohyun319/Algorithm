# silver1-11048. 이동하기
import sys
put = sys.stdin.readline

# (1,1)에서 (N,M)으로 이동할 때 가져올 수 있는 사탕 개수 최대값
# 오른쪽, 아래, 대각선(오른쪽아래)로 이동 가능
# 미로 밖으로 못나감

n, m = map(int, put().split())
array = []
for i in range(n):
  array.append(list(map(int, put().split())))

# i j j j 
# i
# i

# 열(j)마다 돌아가며 행(i) 확인
# 첫째 열에 위치해있는 상황이라 그 다음 열부터 검사
for j in range(1, m):
  for i in range(n):
    # 왼쪽위에서 오는 경우 (오른쪽아래로 감)
    if i == 0: rightDown = 0 #맨위라 범위 벗어남
    else: rightDown = array[i-1][j-1]
    # 위에서 오는 경우 (아래로 감)
    if i == n-1: down = 0 #맨아래라 범위 벗어남
    down = array[i-1][j]    
    # 왼쪽에서 오는 경우 (오른쪽으로 감)
    right = array[i][j-1]
    # 현재 위치에 대한 값을 세 경우 중 최대값으로 갱신
    array[i][j] = array[i][j] + max(right, down, rightDown)

# (n, m)이 가져올 수 있는 사탕의 최댓값으로 갱신돼있음
print(array[n-1][m-1])