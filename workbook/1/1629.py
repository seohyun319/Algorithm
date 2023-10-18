# silver1 - 1629. 곱셈
import sys 
input = sys.stdin.readline

a, b, c = map(int, input().split())
half = a ** (b // 2)

if b == 1:
    print(a % c)
if b % 2 == 0: # 짝수
    print(half * half % c)
if b % 2 == 1: # 홀수
    print(half * half * a % c)


# 시간 초과
# print(a**b%c)

# 10^6 = (10^3)^2 
# 10^6 = (10^3)^2 * 10

# 시간 초과: 곱셈 연산 너무 오래걸려서 절반으로만 자르면 연산 오래걸림. 
# 딱 반만 줄여서 시간 초과
# a, b, c = map(int, input().split())
# half = a ** (b // 2)

# if b == 1:
#     print(a % c)
# if b % 2 == 0: # 짝수
#     print(half * half % c)
# if b % 2 == 1: # 홀수
#     print(half * half * a % c)
