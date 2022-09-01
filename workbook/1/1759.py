# gold5 암호 만들기
import sys 
from itertools import combinations
input = sys.stdin.readline

l, c = map(int, input().split())
strings = input().split()
answer = []
vowels = ['a', 'e', 'i', 'o', 'u']

strings.sort() # 알파벳순으로 하기 위해서 정렬
key_list = list(combinations(strings, l)) # 후보들

for key in key_list:
    vowel_num = 0
    # 각 알파벳이 모음이면 모음 카운트 증가
    for i in key:
        if i in vowels:
            vowel_num += 1
    # 모음 최소 하나, 자음 최소 2개면 가능성 있는 암호
    if vowel_num >= 1 and l - vowel_num >= 2:
        answer.append("".join(key))

print(*answer, sep='\n')
