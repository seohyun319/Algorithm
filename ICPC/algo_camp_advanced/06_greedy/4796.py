# bronze1-4796. 캠핑

import sys
input = sys.stdin.readline

# 캠핑장을 연속하는 P일 중, L일동안만 사용 가능
# 강산이의 휴가는 V일짜리
# 캠핑장을 최대 며칠동안 사용할 수 있는지 

test_case = 1
while True:
    l, p, v = map(int, input().split())
    if l == p == v == 0:
        break
    answer = 0

    full_rest_time = v // p # V일 안에 L일 제한을 몇 번 반복할 수 있는지
    answer += full_rest_time * l
    
    v -= p * full_rest_time
    if l < v: # 사용 가능한 L일보다 남은 휴가 날짜가 더 작음
        answer += l
    else: 
        answer += v 
    
    print(f"Case {test_case}:", answer)
    test_case += 1
