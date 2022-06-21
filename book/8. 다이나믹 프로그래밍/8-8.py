# C8. 다이나믹 프로그래밍 - 실전문제 '효율적인 화폐 구성'

import sys
put = sys.stdin.readline

# 화폐 종류 최소한으로 이용해 가치 합이 m원이 되도록
# 큰 단위 화폐가 작은 단위의 배수가 아니라 그리디 말고 dp로 풀어야

n, m = map(int, put().split())
worth = [int(put()) for _ in range(n)]

# 2, 3원으로 7원 만들기
# d[금액] = 화폐 개수
# d[5]는 d[3] + 1(2원)으로 만들 수 있음
# d[7]는 d[5] + 1(2원)으로 만들 수 있음
# d[7]는 d[7]이랑 d[i-k] + 1 중 최솟값

d = [10001]*(m+1) # dp 테이블 초기화

d[0] = 0 # 0원은 화폐 하나도 안 썼을 때 만들 수 있음
for money in worth:
    for i in range(money, m+1): # 화폐 단위보다 작은 값은 어차피 갱신될 필요도 없음
        # 이전(현재금액 - 화폐단위) 인덱스에 값이 존재하면 현재금액 해당 값 갱신 가능
        if d[i - money] != 10001:
            # 기존 d[i]랑 새로 갱신된 d[i - money] + 1 중 최솟값
            d[i] = min(d[i], d[i - money] + 1)

if d[m] == 10001: print(-1) # M원을 만드는 방법이 존재하지 않으면
else: print(d[m])
        
