# silver2-5525. IOIOI

# PN = N+1개의 I와 N개의 O로 이루어져 있으면, I와 O이 교대로 나오는 문자열
# S안에 PN이 몇 군데 포함되어 있는지

import sys
put = sys.stdin.readline
n = int(put())
m = int(put()) #S의 길이
s = str(put().rstrip()) #문자열 S

cnt = 0
ans = 0
i = 0
while i < m-2:
  if s[i] == 'I' and s[i+1] == 'O' and s[i+2] == 'I':
    cnt += 1
    # print(cnt)
    # 원하는 Pn을 찾음
    if cnt == n: 
      ans += 1
      # 바로 뒤에 이어서 겹쳐서 나올 경우.
      # 'IOIOI'OI
      # IO'IOIOI'
      # 카운트값 1 빼주면 바로 다음에 카운트값 올라가는 경우도 셀 수 있음
      cnt -= 1
    i += 2
  else: 
    cnt = 0 #초기화
    i += 1
print(ans)
