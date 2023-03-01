# silver1-9009. 피보나치

import sys
from itertools import combinations
input = sys.stdin.readline

# 피보나치 수들의 합이 주어진 정수와 같게 되는 최소 개수의 서로 다른 피보나치 수 구하기
# 최소 개수 되려면 제일 큰 값부터 넣어보면 됨

fibonacci = [0]*50
fibonacci[0] = 0
fibonacci[1] = 1
for i in range(2, 50):
    fibonacci[i] = fibonacci[i-1] + fibonacci[i-2]
fibonacci.sort(reverse=True)


t = int(input()) 
for _ in range(t):
    num = int(input()) 
    answer_list = []
    for fibo_num in fibonacci:
        if fibo_num <= num and num != 0: # num이 0이 아닌 한도 내에서 가장 큰 피보나치 수
            answer_list.append(fibo_num)
            num -= fibo_num
    print(*sorted(answer_list))

