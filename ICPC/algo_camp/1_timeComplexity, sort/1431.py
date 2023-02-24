# silver3-1431. 시리얼 번호

import sys
input = sys.stdin.readline

# 1. 길이 짧은 것부터 
# 2. 길이 같으면 자리수 합 작은 것부터 (숫자만 더함)
# 3. 사전순. 숫자가 알파벳보다 사전순으로 작음. 

n = int(input())
serial_nums = [list(input().rstrip()) for _ in range(n)]
num_info = []

# 정렬 기준 여러 개 -> 정렬 기준에 해당하는 내용 각각 커버

for serial in serial_nums:
    temp_sum = 0 # 각 자리수 합
    for alpa_num in serial: # 알파벳 혹은 숫자 한 글자
        if alpa_num.isdigit(): # 숫자이면 더함
            temp_sum += int(alpa_num)    
    num_info.append([len(serial), temp_sum, serial]) # 길이, 자리수 합, 시리얼 번호

num_info.sort(key=lambda x:(x[0], x[1], x[2]))

for i in range(n):
    print(*num_info[i][2], sep='') 
