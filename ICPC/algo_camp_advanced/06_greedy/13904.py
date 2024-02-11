# gold3-13904. 과제

import sys
input = sys.stdin.readline

# 하루에 과제 하나 수행 가능
# 마감일이 지난 과제는 점수를 받을 수 없음
# 얻을 수 있는 점수의 최댓값

n = int(input())
day_score_list = [list(map(int, input().split())) for _ in range(n)] # 과제 마감일까지 남은 일수, 과제의 점수

days = [0]*1001
day_score_list.sort(key=lambda x: -x[1])

answer = 0
for day, score in day_score_list:
    for i in range(day, 0, -1):
        # 뒤부터 비어있는 날짜에 넣음
        if days[i] == 0:
            days[i] = 1
            answer += score
            break

print(answer)
