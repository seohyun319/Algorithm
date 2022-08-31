# silver2 스타트와 링크
import sys 
from itertools import combinations # 조합 
input = sys.stdin.readline

n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]
all_people = list(range(n)) # 전체 사람 나열
teams = list(combinations(all_people, n//2)) # 팀 구성 경우의 수
min_num = 20*100 + 1

for start_team in teams:
    start, link = 0, 0 # 각 능력치 총합
    link_team = set(all_people) - set(start_team)
    start_combi = list(combinations(start_team, 2)) # 스타트팀끼리의 조합
    link_combi = list(combinations(link_team, 2)) # 링크팀끼리의 조합    
    
    for people in start_combi:
        start += s[people[0]][people[1]]
        start += s[people[1]][people[0]]
    for people in link_combi:
        link += s[people[0]][people[1]]
        link += s[people[1]][people[0]]
    
    min_num = min(min_num, abs(start - link))
    
print(min_num)