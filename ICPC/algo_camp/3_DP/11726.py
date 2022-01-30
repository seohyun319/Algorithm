# silver3-11726. 2×n 타일링

import sys
put = sys.stdin.readline

# 2×n 크기의 직사각형을 1×2, 2×1 타일로 채우는 방법의 수를 구하기

n = int(put())
cnt = 0

# n = 1 -> 세로의 1개
# n = 2 -> 세로 / 가로1의 2개
# n = 3 -> 세로 / 가로2의 3개
# n = 4 -> 세로 / 가로3 + 가로가로1의 5개
# n = 5 -> 세로 / 가로4 + 가로가로3의 8개
# n = 6 -> 세로 / 가로5 + 가로가로6 + 가로가로가로1의 13개
# 피보나치인데..?

d= [0]*1001
d[1] = 1
d[2] = 2
for i in range(3, n+1):
  d[i] = d[i-1] + d[i-2]

# 2×n 크기의 직사각형을 채우는 방법의 수를 10,007로 나눈 나머지를 출력한다.
print(d[n]%10007)
