# C10. 그래프 이론 - 실전 문제 '커리큘럼'

from collections import deque
import sys
# import copy
put = sys.stdin.readline

# 노드의 개수 입력 받기
v = int(put())
# 모든 노드에 대한 진입차수는 0으로 초기화
indegree = [0] * (v + 1)
# 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트 초기화
graph = [[] for i in range(v + 1)]
# 각 강의 시간을 0으로 초기화
time = [0] * (v + 1)

# 방향 그래프의 모든 간선 정보를 입력 받기
for i in range(1, v+1): # v개의 강의
    data = list(map(int, input().split()))
    time[i] = data[0] # data 첫 번째는 강의 시간
    for x in data[1:-1]:
        # 진입 차수를 1 증가
        indegree[i] += 1
        graph[x].append(i) # 정점 A에서 B로 이동 가능

# 위상 정렬 함수
def topology_sort():
    # 해당 강의 수강 시간 담아둠
    result = time[:] # 알고리즘 수행 결과를 담을 리스트
    # result = time[:]은 deep copy
    # result = time은 shallow copy
    # result = copy.deepcopy(time) # 리스트에 단순히 대입 연산하면 값 변경될 때 문제 발생해 딥카피 사용
    q = deque() # 큐 기능을 위한 deque 라이브러리 사용

    # 처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입
    for i in range(1, v + 1):
        if indegree[i] == 0:
            q.append(i)

    # 큐가 빌 때까지 반복
    while q:
        # 큐에서 원소 꺼내기
        now = q.popleft()
        result.append(now)
        # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기
        for i in graph[now]:
            result[i] = max(result[i], result[now] + time[i])
            indegree[i] -= 1
            # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
            if indegree[i] == 0:
                q.append(i)

    # 위상 정렬을 수행한 결과 출력
    for i in range(1, v + 1):
        print(result[i])

topology_sort()