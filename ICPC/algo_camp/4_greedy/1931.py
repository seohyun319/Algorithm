# silver2-1931. 회의실 배정

import sys
put = sys.stdin.readline

# 각 회의가 겹치지 않게 하면서 회의실을 사용할 수 있는 회의의 최대 개수

n = int(put())
meet = [list(map(int, put().split())) for _ in range(n)]
#x[1](끝나는 시간) 기준으로 먼저 정렬 후 x[0](시작 시간) 기준으로 정렬
meet.sort(key=lambda x: (x[1], x[0])) 
cnt = 1 #첫번째 회의 배정해서 1부터 시작
end = meet[0][1] #첫번째 회의의 끝나는 시간
for i in range(1, n): #첫번째 회의는 확정이라 그 다음부터 봄
  if end <= meet[i][0]: #앞 회의의 끝나는 시간보다 다음 회의의 시작 시간이 늦으면
    end = meet[i][1] #다음 회의 끝나는 시간으로 end값 갱신
    cnt += 1
print(cnt)
