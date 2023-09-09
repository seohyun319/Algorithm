# silver2-14713. 앵무새
# for word in written_sentence로 하고 written_sentence.popleft() 했더니 for문 중간에 배열이 달라져서 deque mutated during iteration 에러.

import sys
from collections import deque
input = sys.stdin.readline

# written_sentence가 다음 규칙 이용해 나올 수 있는 문장인지 판별
# 1. 한 앵무새는 한 문장을 기억하고 있다. 문장은 여러 단어로 이루어져 있는데, 앵무새는 이 단어들을 순서대로 말한다.
# 2. 한 앵무새가 단어를 말하고 그다음 단어를 말하기 전에는 약간의 간격이 있는데, 이때 다른 앵무새가 말을 가로채고 자신의 문장을 말할 수 있다.
# 3. 한 앵무새가 단어를 말하는 도중에는, 다른 앵무새가 말을 가로채지 않는다.
# 4. 어떤 단어도 앵무새가 말하는 모든 문장을 통틀어 2번 이상 등장하지 않는다.

n = int(input())
parrot_sentences = [deque(input().split()) for _ in range(n)] # 앵무새가 순서대로 말하는 단어
written_sentence = deque(input().split()) # 여러 앵무새들이 말하는 걸 들리는 대로 받아적은 단어
idx, not_written = 0, 0 # 앵무새 인덱스, 청자가 적지 못한 단어를 가진 앵무새 수

while written_sentence: 
    if parrot_sentences[idx] and written_sentence[0] == parrot_sentences[idx][0]: # parrot_sentences가 존재하고 각 첫 단어가 일치
        parrot_sentences[idx].popleft()
        written_sentence.popleft()
        not_written = 0 # 적음
    else: 
        if not_written == n: break # 모두 다 제대로 못 적음
        else: 
            not_written += 1
            idx += 1 # 이번 앵무새에서는 볼 거 더 없으니까 다음 앵무새 봄
            if idx == n: idx = 0 # 못 적은 단어가 있는데 인덱스가 마지막까지 옴 -> 다시 첫 앵무새부터

is_empty = 0 # 앵무새가 말한 걸 모두 적어서 남은 말할 게 없음
for i in range(n):
    if not parrot_sentences[i]: is_empty += 1

if not written_sentence and is_empty == n: print("Possible")
else: print("Impossible")
