# C11. GREEDY - 기출 문제 '곱하기 혹은 더하기'

import sys
input = sys.stdin.readline

# 문자열 S를 왼쪽부터 하나씩 확인하며 사이에 연산자(+, x) 넣어 만들 수 있는 가장 큰 수 구하기
# 연산은 우선순위 상관 없이 왼쪽부터 순서대로임. 

s = input().rstrip()

# 0, 1일 때만 더하고 나머지는 곱하면 제일 크게 나옴
# 0 곱하면 아예 0으로 만들어버리고 1 곱하면 그대로니 1이라도 더하는 게...
result = int(s[0]) # 처음 값 넣고 시작
for i in range(1, len(s)): # 처음 값 넣었으니까 해당 인덱스 뺌
    if int(s[i]) <= 1 or result <= 1:
        result += int(s[i])
    else: result *= int(s[i])
    
    print(result)


# 이런 식으로 result 초기값을 고민했는데 첫 번째 값을 넣어주는 게 인덱스 관련해서 깔끔하게 나옴
# if int(s[0]) == 0: result = 0
# else: result = 1 # 초기값 0이면 곱셈이 무조건 0 나옴
# result = 1 # 초기값 0이면 곱셈이 무조건 0 나옴