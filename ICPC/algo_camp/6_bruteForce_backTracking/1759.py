# gold5-1759. 암호 만들기 

import sys
input = sys.stdin.readline

# 암호는 서로 다른 L개의 알파벳 소문자들로 구성되며 최소 한 개의 모음(a, e, i, o, u)과 최소 두 개의 자음으로 구성
# 암호는 알파벳순 정렬됨
# 사용했을 법한 문자의 종류 C가지가 주어졌을 때, 가능성 있는 암호 모두 구하기

l, c = map(int, input().split())
string = list(map(str, input().split()))
vowels = ["a", "e", "i", "o", "u"]
array = []

string.sort()

def check(answer):
    vowel_cnt = 0
    consonant_cnt = 0
    for x in answer:
        if x in vowels:
            vowel_cnt += 1
        else: 
            consonant_cnt += 1
    if vowel_cnt >= 1 and consonant_cnt >= 2:
        return True
    return False

def back(i):
    if len(array) == l:
        if check(array):
            print(*array, sep='')
            return
    for idx in range(i, c):
        if string[idx] not in array:
            array.append(string[idx])
            back(idx + 1)
            array.pop()

back(0)
