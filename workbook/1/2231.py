# bronze2 - 2231. 분해합
import sys 
input = sys.stdin.readline

n = int(input())
for num in range(1, n+1):
    next = num
    for i in str(num):
        next += int(i)
    if next == n:
        print(num) # 직전 수 == 생성자
        break
    if num == n: # 끝까지 왔는데 break에 안 걸림 == 없는 거임
        print(0) 