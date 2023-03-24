# gold5-2866. 문자열 잘라내기

import sys
input = sys.stdin.readline

# 테이블을 세로로 읽어 문자열 만들 수 있음
# 가장 위 행 지워도 열에서 중복 문자열 없으면 가장 위 행 지워주고 카운트 1 증가
# 중복 문자열 있으면 카운트 출력 후 종료

r, c = map(int, input().split()) # 테이블 행, 열 개수
table = [list(map(str, input().rstrip())) for _ in range(r)] 
count = 0
string_list = []    

# 세로로 읽어 문자열 만듦
for j in range(c):
    string = ""
    for i in range(r):
        string += table[i][j]
    string_list.append(string)

for _ in range(r): 
    # 가장 위 행 지워줌
    for num in range(c):
        string_list[num] = string_list[num][1:]
    # 중복 제거한 거랑 안 한 거랑 개수가 다르면 중복이 있는 것
    if (len(set(string_list)) != len(string_list)):
        print(count)
        exit()
    else: count += 1
print(count)
