# 8. 그래프 이론 (UnionFind, MST, 위상 정렬)

- [서로소 집합](#서로소-집합)
- [신장 트리](#신장-트리)
  - [크루스칼 알고리즘](#크루스칼-알고리즘)
  - [프림 알고리즘](#프림-알고리즘)
- [위상 정렬](#위상-정렬)

## 서로소 집합

- 서로소 집합: 공통 원소가 없는 두 집합
- 서로소 집합 자료구조: 서로소 부분 집합들로 나누어진 원소들의 데이터를 처리하기 위한 자료구조
- 서로소 집합 알고리즘

  - : union-find. 합집합 찾기. 서로소 집합(Disjoint-Set) 알고리즘.
  - 여러 개의 노드가 존재할 때 노드 두 개 선택해서 현재 이 두 노드가 같은 그래프에 속하는지 판별
    - `union`: 합집합. 2개의 원소가 포함된 집합을 하나의 집합으로 합치는 연산
      1. union 연산을 확인해 서로 연결된 두 노드 A, B 확인
         1. A와 B의 루트 노드 A’, B’를 각각 찾음
         2. A’를 B’의 부모 노드로 설정 (B’가 A’를 가리키도록) - 주로 더 작은 원소가 부모 노드
      2. 모든 union 연산을 처리할 때까지 1번 과정 반복 → 각각 루트 노드 찾아서 더 큰 루트 노드가 더 작은 루트 노드 가리키게 됨.
    - `find`: 찾기. 특정한 원소가 속한 집합이 어떤 집합인지 루트 노드 알려주는 연산
  - 서로소 집합 알고리즘 (경로 압축 적용)

    ```python
    # 특정 원소가 속한 집합을 찾기
    def find_parent(parent, x):
        # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
        if parent[x] != x:
            parent[x] = find_parent(parent, parent[x])
        return parent[x]

    # 두 원소가 속한 집합을 합치기
    def union_parent(parent, a, b):
        a = find_parent(parent, a)
        b = find_parent(parent, b)
        if a < b:
            parent[b] = a
        else:
            parent[a] = b

    # 노드의 개수와 간선(Union 연산)의 개수 입력 받기
    v, e = map(int, input().split())
    parent = [0] * (v + 1) # 부모 테이블 초기화하기

    # 부모 테이블상에서, 자기 자신을 부모로 가지도록 설정
    for i in range(1, v + 1):
        parent[i] = i

    # Union 연산을 각각 수행
    for i in range(e):
        a, b = map(int, input().split())
        union_parent(parent, a, b)

    # 각 원소가 속한 집합 출력하기
    print('각 원소가 속한 집합: ', end='')
    for i in range(1, v + 1):
        print(find_parent(parent, i), end=' ')

    print()

    # 부모 테이블 내용 출력하기
    print('부모 테이블: ', end='')
    for i in range(1, v + 1):
        print(parent[i], end=' ')
    ```

  - 경로 압축(Path Compression)
    - Find 연산 시 루트 노드를 찾는 과정에서 만나는 경로 상의 모든 원소가 대푯값을 바로 가리키게 함
      ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/92fb004c-eb1e-4919-93fe-a4461caa8a23/Untitled.png)
    - 최악 시간복잡도 𝑂(𝑁) → 𝑂(1)로 만들어줌
      - 기존 코드
        ```python
        # 특정 원소가 속한 집합을 찾기
        def find_parent(parent, x):
            # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
            if parent[x] != x:
                return find_parent(parent, parent[x])
            return x
        ```
      - 개선 코드 (경로압축 적용)
        ```python
        # 특정 원소가 속한 집합을 찾기
        # 개선: 경로 압축 기법 적용. find 함수 재귀적 호출해 부모 테이블값 갱신
        def find_parent(parent, x):
            # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
            if parent[x] != x:
                parent[x] = find_parent(parent, parent[x])
            return parent[x]
        ```
    - 경로 압축 방법 적용한 서로소 집합 알고리즘의 시간 복잡도: $O(V+M(1+log_{2-M/V}V))$
      - 노드 개수가 V개이고, 최대 V-1개의 union 연산과 M개의 find 연산이 가능할 때.

- 서로소 집합을 활용한 무방향 그래프 내에서의 사이클 판별

  1. 각 간선을 확인하며 두 노드의 루트 노드 확인
     1. 루트 노드가 서로 다르다면 두 노드에 대해 union 연산 수행
     2. 루트 노드가 서로 같다면 사이클(cycle) 발생한 것
  2. 그래프에 포함돼있는 모든 간선에 대해 1번 과정 반복

  - 서로소 집합을 활용한 사이클 판별 소스 코드

    ```python
    # 특정 원소가 속한 집합을 찾기
    def find_parent(parent, x):
        # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
        if parent[x] != x:
            parent[x] = find_parent(parent, parent[x])
        return parent[x]

    # 두 원소가 속한 집합을 합치기
    def union_parent(parent, a, b):
        a = find_parent(parent, a)
        b = find_parent(parent, b)
        if a < b:
            parent[b] = a
        else:
            parent[a] = b

    # 노드의 개수와 간선(Union 연산)의 개수 입력 받기
    v, e = map(int, input().split())
    parent = [0] * (v + 1) # 부모 테이블 초기화하기

    # 부모 테이블상에서, 부모를 자기 자신으로 초기화
    for i in range(1, v + 1):
        parent[i] = i

    cycle = False # 사이클 발생 여부

    for i in range(e): # 모든 간선 하나씩 확인
        a, b = map(int, input().split())
        # 사이클이 발생한 경우 종료
        if find_parent(parent, a) == find_parent(parent, b):
            cycle = True
            break
        # 사이클이 발생하지 않았다면 합집합(Union) 연산 수행
        else:
            union_parent(parent, a, b)

    if cycle:
        print("사이클이 발생했습니다.")
    else:
        print("사이클이 발생하지 않았습니다.")
    ```

  - 방향 그래프에서의 사이클 여부는 DFS로 판별 가능

## 신장 트리

- 신장spanning 트리: 하나의 그래프가 있을 떄 모든 노드를 포함하면서 사이클이 존재하지 않는 ‘부분 그래프’
  - 트리이기 위해서 모든 노드간에 경로가 있음
    → 간선 개수 = 정점 개수 - 1
  - 유일하지 않음
  - 신장트리 가중치(비용): 간선 가중치의 합
- 최소 신장 트리(**MST**) 알고리즘: 신장 트리 중에서 최소 비용으로 만들 수 있는 신장 트리를 찾는 알고리즘

### 크루스칼 알고리즘

- 대표적인 최소 신장 트리 알고리즘. 가장 적은 비용으로 모든 노드 연결 가능
- 그리디 알고리즘으로 분류
- 순서
  1. 간선 데이터를 리스트에 담고 비용에 따라 오름차순 정렬
  2. (거리가 짧은 간선부터) 간선을 하나씩 확인하며(비용 작은 순) 현재의 간선이 사이클 발생시키는지 확인
     1. 사이클이 발생 X → 최소 신장 트리에 포함 O (union 연산)
     2. 사이클이 발생 O → 최소 신장 트리에 포함 X
  3. 모든 간선에 대해 2번의 과정 반복
- 간선E의 개수 = 노드V의 개수 - 1
- 최소신장트리에 포함돼있는 간선 비용만 모두 더하면 그 값이 최종 비용.
- 크루스칼 알고리즘 소스 코드

  ```python
  # 특정 원소가 속한 집합을 찾기
  def find_parent(parent, x):
      # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
      if parent[x] != x:
          parent[x] = find_parent(parent, parent[x])
      return parent[x]

  # 두 원소가 속한 집합을 합치기
  def union_parent(parent, a, b):
      a = find_parent(parent, a)
      b = find_parent(parent, b)
      if a < b:
          parent[b] = a
      else:
          parent[a] = b

  # 노드의 개수와 간선(Union 연산)의 개수 입력 받기
  v, e = map(int, input().split())
  parent = [0] * (v + 1) # 부모 테이블 초기화하기

  # 모든 간선을 담을 리스트와, 최종 비용을 담을 변수
  edges = []
  result = 0

  # 부모 테이블상에서, 부모를 자기 자신으로 초기화
  for i in range(1, v + 1):
      parent[i] = i

  # 모든 간선에 대한 정보를 입력 받기
  for _ in range(e):
      a, b, cost = map(int, input().split())
      # 비용순으로 정렬하기 위해서 튜플의 첫 번째 원소를 비용으로 설정
      edges.append((cost, a, b))

  # 간선을 비용순으로 정렬
  edges.sort()

  # 간선을 하나씩 확인하며
  for edge in edges:
      cost, a, b = edge
      # 사이클이 발생하지 않는 경우에만 집합에 포함
      if find_parent(parent, a) != find_parent(parent, b):
          union_parent(parent, a, b)
          result += cost

  print(result)
  ```

- 시간 복잡도: $`O(ElogE)`$ 간선E 정렬 작업이 가장 오래 걸림. 크루스칼 내부에서 사용되는 서로소 집합 알고리즘의 시간 복잡도는 정렬의 시간복잡도보다 작으니까 무시

### 프림 알고리즘

- 다익스트라와 유사
- 정점을 append하는 방식
- 임의의 노드와 인접한 노드 중 비용이 가장 작은 간선 선택
  1. 선택된 후보 간선들 중 가중치가 가장 작은 간선 선택: Priority Queue 사용
  2. 사이클 방지: visit check → 방문 안 했으면 우선순위 큐에 삽입
- 프림 알고리즘 소스 코드

  ```python
  # 코드 출처 https://deep-learning-study.tistory.com/595
  import heapq, collections, sys
  sys.setrecursionlimit(10**6)
  input = sys.stdin.readline

  n, m = map(int,input().split()) # 노드 수, 간선 수
  graph = collections.defaultdict(list) # 빈 그래프 생성
  visited = [0] * (n+1) # 노드의 방문 정보 초기화

  # 무방향 그래프 생성
  for i in range(m): # 간선 정보 입력 받기
      u, v, weight = map(int,input().split())
      graph[u].append([weight, u, v])
      graph[v].append([weight, v, u])

  # 프림 알고리즘
  def prim(graph, start_node):
      visited[start_node] = 1 # 방문 갱신
      candidate = graph[start_node] # 인접 간선 추출
      heapq.heapify(candidate) # 우선순위 큐 생성
      mst = [] # Minimum Spanning Tree
      total_weight = 0 # 전체 가중치

      while candidate:
          weight, u, v = heapq.heappop(candidate) # 가중치가 가장 적은 간선 추출
          if visited[v] == 0: # 방문하지 않았다면
              visited[v] = 1 # 방문 갱신
              mst.append((u,v)) # mst 삽입
              total_weight += weight # 전체 가중치 갱신

              for edge in graph[v]: # 다음 인접 간선 탐색
                  if visited[edge[2]] == 0: # 방문한 노드가 아니라면, (순환 방지)
                      heapq.heappush(candidate, edge) # 우선순위 큐에 edge 삽입

      return total_weight

  print(prim(graph,1))
  ```

- 시간 복잡도: $`O(N^2)`$
  - 정점 N개 \* 정점마다 O(N)만큼 반복
  - 간선 개수 적으면 무조건 크루스칼 사용, 많으면 프림 사용

## 위상 정렬

- 위상 정렬: 방향 그래프의 모든 노드를 ‘방향성에 거스르지 않도록 순서대로 나열하는 것’.
- 정렬 알고리즘의 일종. 순서가 정해져있는 일련의 작업을 차례로 수행해야 할 때 사용 가능
- ex) 선수과목을 고려한 학습 순서 설정. → 그래프상에서 선후 관계가 있다면 위상 정렬 수행해 모든 선후 관계 지키는 전체 순서 계산 가능
- **진입차수**: 특정 노드로 ‘들어오는’ 간선의 개수.
- 위상 정렬 알고리즘 순서
  1. 진입차수가 0인 노드를 큐에 넣음
  2. 큐가 빌 때까지 다음의 과정 반복
     1. 큐에서 원소를 꺼내 해당 노드에서 출발하는 간선을 그래프에서 제거
     2. 새롭게 진입차수가 0이 된 노드를 큐에 넣음
- 모든 원소를 방문하기 전에(큐에서 원소가 V번 추출되기 전에) 큐가 빈다면 사이클이 존재한다 판단 가능. 사이클이 존재하는 경우 사이클에 포함돼잇는 원소 중 어떤 원소도 큐에 들어가지 못하기 때문.
  - 기본적으로 위상 정렬 문제에서는 사이클이 발생하지 않는다 명시하는 경우가 더 많음
- 위상 정렬 소스 코드

  ```python
  from collections import deque

  # 노드의 개수와 간선의 개수를 입력 받기
  v, e = map(int, input().split())
  # 모든 노드에 대한 진입차수는 0으로 초기화
  indegree = [0] * (v + 1)
  # 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트 초기화
  graph = [[] for i in range(v + 1)]

  # 방향 그래프의 모든 간선 정보를 입력 받기
  for _ in range(e):
      a, b = map(int, input().split())
      graph[a].append(b) # 정점 A에서 B로 이동 가능
      # 진입 차수를 1 증가
      indegree[b] += 1

  # 위상 정렬 함수
  def topology_sort():
      result = [] # 알고리즘 수행 결과를 담을 리스트
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
              indegree[i] -= 1
              # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
              if indegree[i] == 0:
                  q.append(i)

      # 위상 정렬을 수행한 결과 출력
      for i in result:
          print(i, end=' ')

  topology_sort()
  ```

- 시간 복잡도: $`O(V + E)`$ 노드, 간선 모두 확인해서. (차례대로 모든 노드 확인하며 해당 노드에서 출발하는 간선 차례대로 제거해야)

---

참고

- 이것이 취업을 위한 코딩테스트다 - 그래프 이론
- ICPC 신촌 2022 겨울 알고리즘 캠프 - UF&MST
- [프림 알고리즘](https://gmlwjd9405.github.io/2018/08/30/algorithm-prim-mst.html)
- [프림 알고리즘 소스 코드](https://deep-learning-study.tistory.com/595)
