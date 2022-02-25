# gold5-23559. 밥

import sys
put = sys.stdin.readline

# 5,000원짜리 메뉴의 맛 A와 1,000원짜리 메뉴의 맛 B 중 예산 안에 맛의 합을 극대화

n, x = map(int, put().split())
taste = [list(map(int, put().split())) for _ in range(n)]

# 예산 제약 존재, 1000원이 더 맛있는 경우도 존재..
# 맛 수치가 높은 순으로 정렬해 예산 안에서 최적 선택하기
# 맛 수치는 그날의 비교우위. 50 30인 날보다 50 20인 날 5천원짜리 먹는 게 이득
# 일단 천원짜리 다 고른다고 해놓고 예산이 허용되는 한 만족도 높은 순서대로 5천원짜리 껴넣기

# 5천에서 천원짜리 만족도를 뺀 거를 내림차순 정렬
taste.sort(key=lambda x: x[0] - x[1], reverse=True)
# 천원이 만족도 높은 경우는 뒤쪽으로 가서 애초에 천원짜리 다 골랐다 가정해야
leftA = (x - (n*1000)) // 4000 # 천원짜리로만 먹고 남은 돈을 (5000-1000(이미 냈으니 천원 뺌))으로 나눈 몫이 A 먹을 수 있는 횟수
sum = 0 # 만족도 합
for i in taste:
  if leftA > 0 and i[0] > i[1]: # 돈이 가능하고 더 맛있으면 5천원짜리
    sum += i[0]
    leftA -= 1 
  else: sum += i[1] # 안 되면 천원짜리
print(sum)
