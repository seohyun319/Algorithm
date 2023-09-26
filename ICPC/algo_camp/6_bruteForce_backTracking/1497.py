# silver2-1497. 기타콘서트

import sys
input = sys.stdin.readline
from itertools import combinations

# 최대한 많은 곡을 제대로 연주하려고 할 때, 필요한 기타의 최소 개수

n, m = map(int, input().split()) # 기타의 개수 N, 곡의 개수 M
infos = [list(input().split()) for _ in range(n)] # 기타의 이름, 기타가 연주할 수 있는 곡의 정보 (Y는 연주할 수 있는 것이고, N은 없는 것)
playable_songs_idx = [[] for _ in range(n)] # 기타별 연주 가능한 곡 인덱스
max_song_cnt = 0 
max_song_min_guitar_cnt = n # 필요한 기타의 최소 개수 (초기값은 최대 개수인 기타의 전체 개수)

# 최대한 많은 곡 -> 모든 곡이 아닐 수도 있음
# 연주할 곡이 없으면 -1 출력 -> 모든 곡을 연주 불가능한 게 아니라 연주를 하나도 못하는 상황일 때 -1 출력. 

# Y인 곡(연주 가능한 곡)의 인덱스
for i in range(n):
    for j in range(m):
        if infos[i][1][j] == 'Y':
            playable_songs_idx[i].append(j)
    playable_songs_idx[i] = set(playable_songs_idx[i])

# 기타 여러 개 합쳐서 연주 가능한 곡 개수 
def count_guitar_playable_songs(guitar_idx_list):
    guitar_playable_songs = []
    for idx in guitar_idx_list:
        guitar_playable_songs += playable_songs_idx[idx]
    return len(set(guitar_playable_songs))

# 연주할 수 있는 곡이 없음
if count_guitar_playable_songs(range(n)) == 0:
    print(-1)
    exit()

# 기타 1대부터 차례대로 보며 곡의 최대값 갱신
for guitar_cnt in range(1, n+1):
    # 기타의 개수가 1대일 때부터 n대일 때까지 모든 조합 구하기
    for guitar_idx_list in combinations(range(n), guitar_cnt):
        # 현재의 기타 조합으로 연주 가능한 곡 개수
        current_song_cnt = count_guitar_playable_songs(guitar_idx_list)        
        # 현재 연주 가능한 곡 개수가 최대 개수보다 크면 갱신
        if current_song_cnt > max_song_cnt:
            max_song_cnt = current_song_cnt
            max_song_min_guitar_cnt = guitar_cnt

print(max_song_min_guitar_cnt)
