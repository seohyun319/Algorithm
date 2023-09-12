# silver2-23304. 아카라카

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# 주어진 문자열이 아카라카 팰린드롬인지 아닌지 출력
# 아카라카 팰린드롬: 팰린드롬(거꾸로 뒤집어도 같은 문자열)인데 1/2 길이의 접두사와 접미사가 모두 팰린드롬

s = input().rstrip()

def is_akaraka_pallendrom(string):
    if len(string) == 1: return True
    half_len = len(string) // 2
    if string != string[::-1]:
        return False
    left = string[: half_len]
    right = string[-half_len :]
    if left != right:
        return False
    if not is_akaraka_pallendrom(left): 
        return False
    
    return True

if is_akaraka_pallendrom(s):
    print("AKARAKA")
else: print("IPSELENTI")
