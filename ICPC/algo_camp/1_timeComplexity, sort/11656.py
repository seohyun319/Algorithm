# silver4-11656. 접미사 배열

# 문자열의 모든 접미사 사전순 정리 후 출력

s = input() #문자열 S
list=[]
for i in range(len(s)):
  list.append(s[i:])
for a in sorted(list):
  print(a)
