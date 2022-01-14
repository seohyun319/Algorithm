# silver2-18870. 좌표 압축

# X1, X2, ..., Xn 자기자신보다 작은 좌표 개수

import sys
put = sys.stdin.readline
n = int(put())
nums = list(map(int, put().split())) 

# 중복 제거한 리스트(오름차순) 만들기
# 그 리스트 돌면서 몇 번째인지 인덱스 프린트

sortNum = sorted(list(set(nums))) #set은 중복 제거해줌
# 딕셔너리 key는 값, value는 인덱스
sortNum = {sortNum[i]:i for i in range(len(sortNum))}
for i in nums:
  print(sortNum[i], end=' ')
