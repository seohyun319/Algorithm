# bronze2-11091. 알파벳 전부 쓰기

# 팬그램(a~z의 26개 알파벳을 최소 한 번씩 모두 사용한 문장) 판별

import sys
put = sys.stdin.readline
n = int(put()) 

for _ in range(n):
  # 대소문자 구분 X => 소문자로 만들어주기
  miss = [] #나타나지 않은 문자 담을 리스트
  sentence = put().lower()
  for i in range(97, 123): #chr(97)=='a', chr(122)=='z'
    if sentence.find(chr(i)) == -1: #해당 알파벳을 문장에서 못 찾으면
      miss.append(chr(i))
  # miss에 아무것도 안 담기면 모든 알파벳이 사용된 팬그램이라는 뜻
  if miss == []:
    print('pangram')
  else: 
    print('missing ', end='')
    print(''.join(miss))
  