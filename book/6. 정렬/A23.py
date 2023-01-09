# C13. 정렬 - 기출 문제 '국영수'

import sys
input = sys.stdin.readline

# 성적 정렬해 이름 출력: 국어 감소 순 - 영어 증가 순 - 수학 감소 순 - 이름 사전 증가 순

n = int(input())
people_scores = [input().split() for _ in range(n)] # 이름, 국어, 영어, 수학

people_scores.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for i in range(n):
    print(people_scores[i][0])