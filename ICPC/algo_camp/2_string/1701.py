# gold3-1701. Cubeditor

import sys
input = sys.stdin.readline

# 문자열에서 두 번 이상 나오는 부분문자열 중 가장 긴 길이 출력

# abcabc : 3 abc
# ababcabab : 2 ab

string = input().rstrip()
result = 0

# 매칭이 실패했을 때 얼마나 점프해야하는지를 접두사 접미사가 일치하는 것 기준으로 길이 알려줌.
def make_table(pattern):
    table = [0] * len(pattern)
    j = 0
    for i in range(1, len(pattern)):
        # 따라가다가 j가 i와 다르면 j를 직전으로 돌림(j-1의 테이블 값으로 j를 변경)
        while j > 0 and pattern[i] != pattern[j]:
            j = table[j - 1] 
        # i와 j가 가리키는 값이 같으면 숫자 1 증가시켜서 그 다음 문자열까지 같은지 봄
        # 일치하면 i와 j 둘다 증가, 아니면 i만 증가
        if pattern[i] == pattern[j]:
            j += 1
            table[i] = j 
    return table

for i in range(len(string)):
    sub_string = string[i:]
    result = max(result, max(make_table(sub_string)))

print(result)
