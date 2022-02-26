# silver2-20921. 그렇고 그런 사이

import sys
put = sys.stdin.readline

# 왼쪽 수가 오른쪽보다 큰 경우(그렇고 그런 사이)가 k가지여야 함

n, k = map(int, put().split()) # n명, k개의 경우 만들기
answer = []
visited = [0] * (n+1)
maxN = n

# 첫 번째 사람한테 n번(제일 높은 값) 쪽지 주면 n-1만큼 생김

while k:
    if maxN - 1 <= k: # 만들어야하는 수보다 생길 수가 작을 때
        visited[maxN] = 1 # 방문 처리
        k -= (maxN - 1) # 생긴 수만큼 k(만들어야 하는 수) 소진
        answer.append(maxN) # 높은 번호의 쪽지 줌
    # (if문) 해당 번호 쪽지 줬으니까 소진됨 -> 그다음 제일 큰 수로 갱신
    # (if문 x) 생길 수를 1 줄여서 다시 도전
    maxN -= 1 

for i in range(1, n+1):
    if not visited[i]: 
        answer.append(i) # 낮은 수부터 순차적 배치

print(' '.join(map(str, answer)))
