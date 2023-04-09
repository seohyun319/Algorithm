# 5. 분할정복 - 이진탐색

- [분할 정복](#분할-정복)
- [순차 탐색](#순차-탐색)
- [이진 탐색 (이분 탐색, Binary Search)](#이진-탐색-이분-탐색-binary-search)
- [lower_bound & upper_bound](#lowerbound--upperbound)
- [좌표압축](#좌표압축)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/ca8bcf47-4500-439b-8c53-8ae0729fd070/Untitled.png)

# 분할 정복

- 매개변수 탐색 (Parametric Search)
  - 결정 문제(O/X)로 최적화 문제(최대값 등의 요구사항 있는 문제)를 푸는 기법
  - 특정 파라미터를 기준으로 조건을 만족하는 부분과 만족하지 않는 경계점 찾기
    > 어떤 시점부터 만족(T)과 불만족(F)이 양분(둘로 나눠짐)됨. 이진 탐색과 비슷하게 풀 수 있음.
    > 최적화 문제보다 쉬운 결정 문제로 쪼개기
- 분할 정복 (Divide & Conquer, DnC)
  - 문제를 (비슷한 크기의) 둘 이상의 부분 문제로 나눈 뒤 (Divide)
    각 문제에 대한 답을 계산하고 (Conquer)
    원래 문제에 대한 답으로 병합 (Merge) > 알고리즘의 하나라기보다는 설계기법. >
- cf) 동적계획법 (Dynamic Programming)은 중복되는 부분 문제(Overlapping Subproblems) O (→ 메모이제이션으로 해결)
  - 분할 정복의 부분 문제는 크기만 작아지고 원래 문제와 성격은 비슷
  - 중복 부분 문제 X
- 사용 예시

  1.  이진탐색
      1. Divide: 탐색 범위 절반으로 나눔 (탐색값 찾으면 종료)
      2. Conquer:
         1. 중간값 < 탐색값 ⇒ 왼쪽 확인
         2. 중간값 > 탐색값 ⇒ 오른쪽 확인
  2.  퀵정렬, 병합정렬 $`O(NlogN)`$
      1. Divide: 수열을 절반으로 나눔
      2. Conquer: 정렬
      3. Merge: 부분적으로 정렬된 수열의 결과 종합
  3.  분할정복을 이용한 거듭제곱 (Exponentiation by Squaring)
      - base case: b==0 → 1 리턴
      - 홀수인 경우: -1해서 짝수로 만들고 a 곱하기
      - 짝수인 경우: 그 절반에 해당하는 값 구하고 두번 곱하기
        ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/ae478e83-cd65-4df2-8c67-31cb68e1aacb/Untitled.png)
        - 𝑂(𝑛) 을 𝑂(log 𝑛)으로
  4.  행렬 거듭 제곱

      - 𝑁 × 𝑁 크기 행렬 𝐴의 거듭제곱 𝐴$^𝑚$
      - 𝑎$^0$ = 1, 𝐴$^0$ = 𝐼, (𝐼: 𝑖𝑑𝑒𝑛𝑡𝑖𝑡𝑦 𝑚𝑎𝑡𝑟𝑖𝑥)
        정방행렬에 대한 0제곱은 I(Identity matrix, 단위행렬)이다
        ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/cd25bf43-7010-4959-acb6-c06c54f034f1/Untitled.png)

            ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/dacec8c9-d7a1-41f8-a464-eb1598e817cd/Untitled.png)

            ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/b9560ef7-f16f-46e3-a639-58f04989994d/Untitled.png)

            - 시간 복잡도
                - 정방 행렬 곱셈 𝑂(𝑁$^3$) * 거듭제곱 𝑂(log 𝑚)
                ⇒ 𝑂(𝑁$^3$log 𝑚)

# 순차 탐색

- 리스트 안에 있는 특정 데이터를 찾기 위해 앞에서부터 데이처를 차례대로 하나씩 확인하는 방법
- 장점: 시간만 충분하다면 데이터가 아무리 많아도 원하는 데이터를 찾을 수 있음
- 코드

  ```python
  # C7. 이진 탐색 - 순차 탐색 소스 코드
  def sequential_search(n, target, array):
      #각 원소를 하나씩 확인하며
      for i in range(n):
          # 현재의 원소가 찾고자하는 원소와 동일한 경우
          if array[i] == target:
              return i + 1 #현재의 인덱스 번호 반환 (0부터 시작하니까 1 더해서 원하는 값으로 표기)

  print("생성할 원소 개수를 입력한 다음 한 칸 띄고 찾을 문자열을 입력하세요.")
  input_data = input().split()
  n = int(input_data[0]) #원소의 개수
  target = input_data[1] #찾고자 하는 문자열

  print("앞서 적은 원소 개수만큼 문자열을 입력하세요. 구분은 띄어쓰기 한 칸으로 합니다.")
  array = input().split()

  # 순차 탐색 수행 결과 출력
  print(sequential_search(n, target, array))
  ```

# 이진 탐색 (이분 탐색, Binary Search)

- 찾으려는 데이터의 중간점 위치에 있는 데이터를 반복적으로 비교해 원하는 데이터 찾음
  - **정렬된 리스트**(sort(a))에서 특정한 값(key)을 찾는 알고리즘
    탐색 구간의 중앙값과의 대소 비교를 통해 다음 탐색구간 설정 > 중앙값과 키값 비교했는데 키값이 더 크면 중앙값보다 작은 부분은 볼 필요 없음 → 탐색 구간이 절반씩 줄어듦 >
  - 탐색 범위를 절반씩 좁혀가며(반으로 쪼개며) 데이터 탐색.
    > 구간을 두개로 나눠 탐색 - 어떤 구간에는 반드시 없다는 게 보장되고 어떤 구간에는 반드시 있다는 게 보장됨
- 주로 탐색 범위가 큰 상황(2000만), 탐색 연산이 반복적으로 요구될 때 사용. 처리해야 할 데이터 개수나 값이 1000만 단위 이상으로 넘어가면 이진탐색처럼 $O(logN)$ 속도 내는 알고리즘 떠올려야.
- 중간점이 실수이면 소수점 이하 버림.
- 시간 복잡도: $`O(logN)`$. 한 번 확인할 때마다 확인하는 원소의 개수가 절반씩 줆.
- 1. 재귀함수를 이용

  ```python
  # C7. 이진 탐색 - 재귀 함수로 구현한 이진 탐색 소스 코드

  def binary_search(array, target, start, end):
      if start > end:
          return None
      mid = (start + end) // 2  # 몫 구함
      # 찾은 경우 중간점 인덱스 반환
      if array[mid] == target:
          return mid
      # 중간점의 값보다 찾고자 하는 값이 적은 경우 왼쪽 확인
      elif array[mid] > target:
          return binary_search(array, target, start, mid - 1)
      # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
      else:
          return binary_search(array, target, mid + 1, end)

  # n(원소의 개수)과 target(찾고자하는 문자열) 입력받기
  n, target = list(map(int, input().split()))
  # 전체 원소 입력받기
  array = list(map(int, input().split()))

  #이진 탐색 수행 결과 출력
  result = binary_search(array, target, 0,  n-1)
  if result == None:
      print("원소가 존재하지 않습니다")
  else:
      print(result + 1)
  ```

- 2. 반복문 이용 (기본 코드형 외우기)

  ```python
  # C7. 이진 탐색 - 반복문으로 구현한 이진 탐색 소스 코드

  def binary_search(array, target, start, end):
      while start <= end:
          mid = (start + end) // 2  # 몫 구함
          # 찾은 경우 중간점 인덱스 반환
          if array[mid] == target:
              return mid
          # 중간점의 값보다 찾고자 하는 값이 적은 경우 왼쪽 확인
          elif array[mid] > target:
              end = mid - 1
          # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
          else:
              start = mid + 1
      return None

  # n(원소의 개수)과 target(찾고자하는 문자열) 입력받기
  n, target = list(map(int, input().split()))
  # 전체 원소 입력받기
  array = list(map(int, input().split()))

  #이진 탐색 수행 결과 출력
  result = binary_search(array, target, 0,  n-1)
  if result == None:
      print("원소가 존재하지 않습니다")
  else:
      print(result + 1)
  ```

## lower_bound & upper_bound

- lower_bound
  - key **이상(key포함)**의 값이 처음 나오는 위치
  - ex) a = [2, 3, 5, 7, 11, 11], key = 8,
    lower_bound(a, a + 6, key) – a = 4
- upper_bound
  - key **초과**의 값이 처음 나오는 위치
  - ex) a = [2, 3, 5, 8, 8, 11], key = 8,
    upper_bound(a, a + 6, key) – a = 5

> 찾고자 하는 원소 개수 구할 때 upper_bound - lower_bound 로 구할 수 있음.
> 이렇게하면 R - L +1처럼 다른 연산(+1) 고려 안 해도 됨.

> 리스트에서 없는 수 구하려고 하면 lower_bound와 upper_bound가 같은 주소값 가리킬 것. 그러면 lower_bound - upper_bound = 0 이 될 것.

## 좌표압축

- 좌표 압축(Coordinate Compression)
  - 간격 또는 중복 정보를 제거하여 많은 점 집합을 더 작은 범위에 mapping하는 기법
    - 실제 간격의 정보가 덜 중요할 때
    - 중복값이 많고 상대적인 순서만 알아도 될 때
    - (좌표 상에서) range는 크지만 실제 점 개수(좌표 정보의 개수)는 적을 때
      ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/f5c282e1-8d5e-441d-b9f3-337323d45d93/Untitled.png)
    - python with set, dict
      ```python
      arr2 = sorted(list(set(arr))) # 중복 제거
      # 정렬된 배열의 값과 인덱스를 딕셔너리 형태로 저장, 새 좌표 부여
      dic = {arr2[i] : i for i in range(len(arr2))}
      print(*[dic[i] for i in arr])
      #for i in arr:
      #    print(dic[i], end = ' ')
      ```

---

참고 링크

- [분할 정복](https://hiddenevent.github.io/algorithm/02_Division)
- 이것이 취업을 위한 코딩테스트다 - 이진 탐색
- ICPC 신촌 2022 겨울 알고리즘 캠프 - 이분탐색&분할정복
