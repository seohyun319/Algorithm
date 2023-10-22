# silver3 - 2503. 숫자 야구
import sys 
from itertools import permutations # 순열 만들기
input = sys.stdin.readline

n = int(input()) # 질문한 횟수
num_list = list(permutations([1, 2, 3, 4, 5, 6, 7, 8, 9], 3)) # 모든 경우의 수
for _ in range(n):
    guess, s, b = map(int, input().split()) # 질문한 세 자리 수, 스트라이크, 볼
    guess = list(str(guess)) # 'int' object is not iterable
    remove_cnt = 0 # num_list에서 원소 지운 개수 (for문 돌다가 지워지면 건너뛰는 거 생김)
    
    for i in range(len(num_list)):
        strike, ball = 0, 0
        # 이렇게 수정해야 하는 경우 while문 쓰는 게 좋음
        i -= remove_cnt
        # 각 자리수 일치 여부 확인
        for j in range(3):
            if str(num_list[i][j]) == guess[j]:
                strike += 1
            elif str(num_list[i][j]) in guess:
                ball += 1
        # 스트라이크와 볼 개수가 동시에 일치해야 함
        if not (strike == s and ball == b):
            num_list.remove(num_list[i])
            remove_cnt += 1

print(len(num_list))

# 왜 틀리나 했더니 remove_cnt 처리 안 해줘서 
# 지워지는 데이터만큼 인덱스를 건너뛰는 것처럼 됨...
