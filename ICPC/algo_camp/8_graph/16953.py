# silver2-16953. A → B

import sys
input = sys.stdin.readline

# A를 B로 바꾸는데 필요한 연산의 최솟값
    # 2를 곱한다.
    # 1을 수의 가장 오른쪽에 추가한다. 

a, b = map(int, input().split())
cnt = 1 # 연산 횟수

while a < b:
    last_b_number = b % 10
    if last_b_number == 1:
        b = b // 10 # 가장 오른쪽 1 빼줌
        cnt += 1
    elif last_b_number % 2 == 0: 
        b = b // 2 # 2로 나눔
        cnt += 1    
    else: 
        print(-1)
        exit()
    if a > b: # a == b인 순간에 while문이 끝나지 않고 a > b까지 왔다면 A를 B로 바꾸기 불가능한 것 
        print(-1)
        exit()
print(cnt)



