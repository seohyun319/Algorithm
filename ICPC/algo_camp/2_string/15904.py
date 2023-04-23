# silver5-15904. UCPC는 무엇의 약자일까?

import sys
input = sys.stdin.readline

# 대문자만 뽑았을 때 무조건 UCPC만 나와야 하는 건 아니고 
# UCPCC의 경우도 축약했을 때 UCPC로 축약 가능
# I love UCPC도 UCPC로 축약 가능

string = list(input().rstrip())
upper_list = []
UCPC = ["U", "C", "P", "C"]
index = 0

for spell in string:
    if spell.isupper() and spell == UCPC[index]: # 중간에 다른 게 껴도 UCPC가 순서대로 들어오기만 하면 됨. 
        upper_list.append(spell)
        index += 1
        if index == 4: break # 원하는 결과 다 얻음 (없으면 런타임 인덱스 에러 발생)
if upper_list == UCPC: print("I love UCPC")
else: print("I hate UCPC")

