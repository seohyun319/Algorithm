# silver3-1448. 삼각형 만들기

# N개 중 3개를 선택했을 때, 세 변의 길이 합의 최댓값

import sys
put = sys.stdin.readline
n = int(put()) #빨대 갯수
length = []
for _ in range(n):
  length.append(int(put())) #빨대 길이

# 제일 긴 선분의 길이가 나머지 둘의 합보다 짧을 때 삼각형 성립
# a < b + c
# 내림차순 정렬했을 차례로 세 개가 성립하면 됨. 
# 순차 3개(a b c)가 성립 안 하면 a b d, a b e... 등의 케이스도 성립 불가
# -> 그다음 순서대로 세 개 성립하는지 검사하면 될 듯
# 실패 케이스: 마지막 세 개까지 왔는데 불가능 (-1 출력)

length.sort(reverse=True)
  
for i in range(n-2):
  # 성립하면 총합 출력
  if length[i] < length[i+1] + length[i+2]:
    print(length[i] + length[i+1] + length[i+2])
    break
  # 마지막까지 가도 성립 안 하면 -1 출력 
  if i == n-3:
    if length[i] >= length[i+1] + length[i+2]:
      print("-1")
      