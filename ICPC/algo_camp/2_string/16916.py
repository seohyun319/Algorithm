# gold3-16916. 부분 문자열

import sys
put = sys.stdin.readline

# P가 S의 부분문자열이면 1 출력

# 매칭이 실패했을 때 얼마나 점프해야하는지를 접두사 접미사가 일치하는 것 기준으로 길이 알려줌.
def makeTable(pattern):
  table = [0] * len(pattern)
  j = 0
  for i in range(1, len(pattern)):
    # 따라가다가 j가 i와 다르면 j를 직전으로 돌림(j-1의 테이블 값으로 j를 변경)
    while j > 0 and pattern[i] != pattern[j]:
      j = table[j - 1] 
    # i와 j가 가리키는 값이 같으면 숫자 1 증가시켜서 그 다음 문자열까지 같은지 봄
    # 일치하면 i와 j 둘다 증가, 아니면 i만 증가
    if pattern[i] == pattern[j]:
      j += 1
      table[i] = j 
  return table

# 접두사가 일치하는 한 일치하는 최대 길이만큼 이동(점프)시키는 것 반복
def KMP(parent, pattern):
  table = makeTable(pattern)
  j = 0
  for i in range(len(parent)):
    while j > 0 and parent[i] != pattern[j]:
      j = table[j - 1]
    if parent[i] == pattern[j]:
      # 모든 문자가 일치하는 경우
      if j == len(pattern) - 1:
        return 1
      # 매칭만 이뤄진 거라 매칭이 더 이뤄지는지 계속해서 확인
      else: j += 1

  return 0


s = str(put().rstrip()) 
p = str(put().rstrip()) 
print(KMP(s, p))

