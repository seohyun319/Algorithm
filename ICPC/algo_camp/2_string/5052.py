# gold4-5052. 전화번호 목록

import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    phone_numbers = [list(input().rstrip()) for _ in range(n)]

    has_consistency = True
    phone_numbers.sort()
    for i in range(n - 1):
        number_i_len = len(phone_numbers[i]) 
        # i+1번째 번호를 i번째의 길이까지 봤을 때 i번째 번호랑 동일하면 일관성 없는 것
        if phone_numbers[i] == phone_numbers[i + 1][:number_i_len]:
            has_consistency = False
            print("NO")
            break
    if has_consistency: print("YES")