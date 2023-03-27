# bronze2-4583. 거울상

# 딕셔너리로 만들면 더 빨라질 수 있음. {i:i}, ,, {b:d} {d:b},....

import sys
input = sys.stdin.readline

# 서로 거울상: b, d / p, q
# 자신과 거울상: i, o, v, w, x

self_mirror_list = ["i", "o", "v", "w", "x"]
# 각자의 거울상이 바로 다음에 오게 배치함. 
# pair_mirror_list.index(alphabet)로 찾는 경우 앞부터 찾기 때문에 
# b의 경우 제일 앞에 있는 0번 인덱스가 선택돼
# pair_mirror_list.index(alphabet) + 1은 1번 인덱스인 d가 됨.  
pair_mirror_list = ["b", "d", "b", "p", "q", "p"] 

while True:
    word = input().rstrip()
    if word == "#": break

    mirror_word = []
    for alphabet in word[::-1]: # 거울상이니까 뒤에서부터 확인
        if alphabet in self_mirror_list: 
            mirror_word.append(alphabet)
        elif alphabet in pair_mirror_list: 
            # 각자의 거울상 추가하게 함.
            mirror_word.append(pair_mirror_list[pair_mirror_list.index(alphabet) + 1])
        else: 
            print("INVALID")
            mirror_word = [] # 불가능한 문자 만나기 전에 리스트에 append된 경우 커버용으로 비워줌
            break
    if mirror_word: # 빈 배열 오는 경우 따로 출력하지 않기 위함
        print(*mirror_word, sep='')