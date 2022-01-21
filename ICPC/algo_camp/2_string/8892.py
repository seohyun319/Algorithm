# silver5-8892. 팰린드롬

# 팰린드롬: 어느 방향으로 읽어도 항상 같은 방법으로 읽을 수 있는 단어
# 주어진 단어 중 두 개를 조합해 팰린드롬 만들기

import sys
put = sys.stdin.readline

for _ in range(int(put())): #테스트케이스 개수만큼 for문 돌기
  n = int(put()) #단어의 수
  words = [put().rstrip() for _ in range(n)] #n개의 단어
  newWordList = []
  for i in range(n):
    for j in range(n):      
      if i == j: continue #서로 다른 두 단어를 더하기 위해서 같은 경우 무시
      newWord = words[i] + words[j]
      if newWord == newWord[::-1]:
        newWordList.append(newWord) #가능한 거 중 아무거나 출력하래서 새 리스트에 담음
        # 여기에 아무거나 하나만 출력 위해서 print(newWord)하고 break 했더니
        # newWord를 만들다가 break되는 경우가 생겨서 모든 케이스를 커버 못해서 틀렸던 것
  if newWordList == []: print(0)
  else: print(newWordList[0]) 
