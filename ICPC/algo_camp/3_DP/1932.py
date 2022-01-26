# silver1-1932. 정수 삼각형

import sys
put = sys.stdin.readline

# 층마다 수 하나 선택해 아래층(현재층의 대각선왼쪽/오른쪽 중 하나)으로 내려올 때 선택된 수 합이 최대가 되는 경로

n = int(put())
triangle = [list(map(int, put().split())) for _ in range(n)]

# triangle[0][0]
# triangle[1][0], triangle[1][1]
# triangle[2][0], triangle[2][1], triangle[2][2]
# triangle[3][0], triangle[3][1], triangle[3][2], triangle[3][3]

for i in range(1, n):
  for j in range(len(triangle[i])): #각 줄의 정수 개수
    if j == 0: #맨 왼쪽 줄
      triangle[i][j] += triangle[i-1][j]
    elif j == i: #맨 오른쪽 줄
      triangle[i][j] += triangle[i-1][j-1]
    else:
      triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])
# 마지막줄 보면 합이 쌓였을 텐데 그 중에서 최대값 고르면 됨
print(max(triangle[n-1]))
