# silver1-1946. 신입 사원

import sys
input = sys.stdin.readline

# 서류 면접 중 하나가 다른 사람보다 떨어지지 않는 지원자 수
# A의 서류와 면접이 둘 다 B의 서류와 면접보다 높으면 B는 탈락

t = int(input())
for _ in range(t):
    n = int(input())
    rankings = [list(map(int, input().split())) for _ in range(n)] # 서류 순위, 면접 순위
    cnt = 1 # 기준점 지원자(서류 1등)는 카운트 안 돼서 1부터 시작

    rankings.sort() # 서류 순위순 정렬
    hired = rankings[0][1] # 서류 1등은 일단 무조건 채용됨
    for i in range(1, n): # 서류 2등부터 봄
        if hired > rankings[i][1]:
            cnt += 1
            hired = rankings[i][1]
    print(cnt)
    