# gold5 - 9251. LCS
# LCS는 기법으로 쓰임. 기억해두기. 

import sys 
input = sys.stdin.readline

a = [0] + list(input().rstrip())
b = [0] + list(input().rstrip())
n, m = len(a) - 1, len(b) - 1 # 맨 앞에 0 추가한 건 개수에서 빼줌
dp = [[0] * (m+1) for _ in range(n+1)] 

for i in range(1, n+1):
    for j in range(1, m+1):
        if a[i] == b[j]:
            dp[i][j] = dp[i-1][j-1] + 1
        else: 
            # CAPCAK와 ACAY의 경우 dp[i][j-1]은 2, dp[i-1][j]은 3. 3이 맞음. 왼쪽 말고 위에서 오는 케이스도 커버하기
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[n][m])