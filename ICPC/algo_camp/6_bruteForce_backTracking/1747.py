# silver1-1747. 소수&팰린드롬

import sys, math
input = sys.stdin.readline

# N보다 크거나 같고, 소수이면서 팰린드롬인 수 중에서, 가장 작은 수

n = int(input())

def is_prime_number(x):
    if x == 1: return False # 1은 소수가 아님
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0: # x가 나누어떨어지면 소수 아님
            return False
    return True

def is_palindrome(x):
    string_x = str(x)
    if string_x == string_x[::-1]:
        return True
    else: return False

for i in range(n, 1003002): # n의 최대 입력값인 1,000,000에 맞춰 1000001 넣었더니 틀림: 1000000 입력 시 1003001이 나와야 함
    if is_palindrome(i) and is_prime_number(i): # 팰린드롬 먼저 체크하고 그 중에서 소수 체크하니 3000ms였던 거 300ms 걸림
        print(i)
        break