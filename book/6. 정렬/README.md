# 4. 정렬

- [선택 정렬](#선택-정렬)
- [버블 정렬](#버블-정렬)
- [삽입 정렬](#삽입-정렬)
- [퀵 정렬](#퀵-정렬)
- [계수 정렬](#계수-정렬)
- [병합 정렬](#병합-정렬)
- [정렬 라이브러리](#정렬-라이브러리)

**정렬**: 데이터를 특정 기준에 따라 순서대로 나열하는 것

## **선택 정렬**

: 가장 작은 것을 선택해 제일 앞으로 보냄
(여러 개 중 가장 작은 걸 맨 앞과 바꾸고, 그다음 작은 걸 앞에서 두번째와 바꾸는 과정 반복)
가장 작은 데이터를 앞으로 보내는 과정을 n-1번 반복하면 정렬 완료됨

데이터가 N개일 때 (N + (N-1) + (N-2) + ... + 2) → 등차수열 $(N * (N+1))/2$ 만큼의 연산을 해야 함.

가장 큰 차수만 봤을 땐 N의 제곱. $`O(N^2)`$ 시간복잡도는 빅 O로 표기

모든 원소 다 보고 각 원소를 다른 모든 원소와 비교함.

- 코드

  - c

    ```c
    #define _CRT_SECURE_NO_WARNINGS
    #include <stdio.h>

    int main() {
        int i, j, min, index, temp;
        int array[10] = { 1, 10, 5, 8, 7, 6, 4, 3, 2, 9 };
        for (j = i; j < 10; j++) {
            if (min > array[j]) {
                min = array[j];
                index = j;
            }
        }
        temp = array[i];
        array[i] = array[index];
        array[index] = temp;

        for (i = 0; i < 10; i++) {
            printf("%d ", array[i]);
        }
        return 0;
    }
    ```

  - python

    ```python
    array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

    for i in range(len(array)):
        min_index = i #가장 작은 원소의 인덱스
        for j in range(i+1, len(array)):
            if array[min_index] > array[j]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i] #스와프(:두 변수 위치 변경)

    print(array)
    ```

## **버블 정렬**

: 가까이(옆)에 있는 두 숫자끼리 비교해 더 작은 숫자를 앞으로 보냄

구현은 쉽지만 가장 비효율적. 각 사이클마다 가장 큰 값이 맨 뒤로 보내짐. 실제 수행 시간이 가장 느림.

시간 복잡도 $`O(N^2)`$

- 코드

  ```c
  #define _CRT_SECURE_NO_WARNINGS
  #include <stdio.h>
  #include <stdlib.h>
  #include <string.h>

  int main() {
      int i, j, min, index, temp;
      int array[10] = { 1, 10, 5, 8, 7, 6, 4, 3, 2, 9 };
      for (i = 0; i < 10; i++) {
          for (j = 0; j < 9 - i; j++) {
              if (array[j] > array[j + 1]) {
                  temp = array[j];
                  array[j] = array[j + 1];
                  array[j + 1] = temp;
              }
          }
      }
      for (i = 0; i < 10; i++) {
          printf("%d ", array[i]);
      }
      return 0;
  }
  ```

## **삽입 정렬**

: 가까이(옆)에 있는 두 숫자끼리 비교해 더 작은 숫자를 앞으로 보냄. 특정 데이터를 적정 위치에 '삽입'

당장 왼쪽에 있는 값과 비교해서 위치 바꿈. 왼쪽에 있는 건 이미 정렬됐다고 가정하기에 (그래서 맨 처음에도 두번째 데이터부터 시작함) 자기가 왼쪽에 있는 것보다 크다면 거기에서 멈추면 됨. 멈출 포인트를 알고 있음.

시간 복잡도 $`O(N^2)`$

필요할 때만 위치 바꾸니까 거의 정렬돼있는 경우면 어떤 알고리즘보다도 빠름. (최선의 경우 O(N)의 시간복잡도 가질 수도.

- 코드

  - C

    ```c
    #define _CRT_SECURE_NO_WARNINGS
    #include <stdio.h>
    #include <stdlib.h>
    #include <string.h>

    int main() {
        int i, j, temp;
        int array[10] = { 1, 10, 5, 8, 7, 6, 4, 3, 2, 9 };
        for (i = 0; i < 9; i++) {
            j = i;
            while (array[j] > array[j + 1]) {
                temp = array[j];
                array[j] = array[j + 1];
                array[j + 1] = temp;
                j--;
            }
        }
        for (i = 0; i < 10; i++) {
            printf("%d ", array[i]);
        }
        return 0;
    }
    ```

  - PYTHON

    ```python
    array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

    for i in range(len(array)):
        for j in range(i, 0, -1): #인텍스 i부터 1까지 1씩 감소
            if array[j-1] > array[j]:
                array[j], array[j-1] = array[j-1], array[j] #스와프(:두 변수 위치 변경)
            else: break #자기보다 작은 데이터 만나면 그 위치에서 멈춤

    print(array)
    ```

## **퀵 정렬**

: 특정 값 기준으로 큰 숫자와 작은 숫자를 교환한 후 배열을 반으로 나눔

기준값(피벗)보다 큰 숫자(a)를 왼쪽부터, 작은 숫자(b)를 오른쪽부터 찾음. 찾자마자 큰 값(a)과 작은 값(b)의 위치를 서로 바꿔줌.

p 0 **a** 0 0 **b** 0 0 → p 0 **b** 0 0 **a** 0 0

계속 바꾸다가 왼쪽부터 찾은 큰 숫자가 오른쪽부터 찾은 작은 숫자보다 오른쪽에 있을 때가 있음. (=a b가 아닌 b a 순서. 엇갈렸다.) 그럴 땐 왼쪽에 있는 더 작은 값과 피벗값의 위치를 바꾸면 됨. 이제 해당 피벗값은 정렬 이룸.

p(3) 2 **1(b)** **8(a)** 5 9 6 → **1(b)** 2 p(3) **8(a)** 5 9 6

분할(파티션) 완료: 피벗 이동한 상태에서 피벗보다 왼쪽에 있는 값은 모두 피벗값보다 작고, 오른쪽은 모두 피벗값보다큼.
→ 왼쪽, 오른쪽 리스트 각 피벗 결정해 개별 정렬 수행하면 전체 리스트에 대해 모두 정렬 이루어짐

재귀 함수랑 동작 원리 동일. 종료 조건: 현재 리스트의 데이터 개수가 1개

첫 피벗 값은 주로 제일 왼쪽에 있는 값으로 정함.

시간 복잡도 $`O(NlogN)`$ - 데이터 개수 많을 수록 (다른 정렬과 비교했을 때) 빠르게 동작

(최악의 경우(이미 거의 다 정렬됐을 경우) $`O(N^2)`$ 나올 수도.. 저땐 삽입 정렬 써야 함)

- 코드

  - c

    ```c
    #include <stdio.h>

    int number = 10;
    int data[] = { 1, 10, 5, 8, 7, 6, 4, 3, 2, 9 };

    void show() {
    	int i;
    	for (i = 0; i < number; i++) {
    		printf("%d ", data[i]);
    	}
    }

    void quickSort(int* data, int start, int end) {
    	if (start >= end) { //원소가 1개인 경우 그대로 두기
    		return;
    	}

    	int key = start; //키는 첫 번째 원소(피벗값)
    	int i = start + 1; //왼쪽부터 찾음
    	int j = end; //오른쪽부터 찾음
    	int temp;

    	while (i <= j) { //엇갈릴때까지 반복
    		while (i <= end && data[i] <= data[key]) {//키 값보다 큰 값을 만날 때까지 오른쪽으로
    			i++;
    		}
    		while (j <= start && data[i] <= data[key]) {//키 값보다 작은 값을 만날 때까지 왼쪽으로
    			j--;
    		}
    		if (i > j) { //현재 엇갈린 상태면 키 값과 교체
    			temp = data[j];
    			data[j] = data[key];
    			data[key] = temp;
    		}
    		else { //엇갈리지 않았다면 i와 j를 교체
    			temp = data[i];
    			data[i] = data[j];
    			data[j] = temp;
    		}
    	}
    	quickSort(data, start, j - 1);
    	quickSort(data, j + 1, end);
    }

    int main(void) {
    	quickSort(data, 0, number - 1);
    	show();
    	return 0;
    }
    ```

  - python 1 (직관적 형태, 가장 널리 사용)

    ```python
    array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

    def quick_sort(array, start, end):
        if start >= end: #원소가 1개인 경우 종료
            return
        pivot = start #피벗은 첫 번째 원소
        left = start + 1
        right = end
        while left <= right:
            # 피벗보다 큰 데이터를 찾을 때까지 start+1부터 오른쪽으로 감
            while left <= end and array[left] <= array[pivot]:
                left += 1
            # 피벗보다 작은 데이터를 찾을 때까지 end부터 왼쪽으로 감
            while right > start and array[right] >= array[pivot]:
                right -= 1
    				# 엇갈렸다면(왼쪽부터 찾은 큰 숫자가 오른쪽부터 찾은 작은 숫자보다 오른쪽에 있을 때)
    				# 왼쪽에 있는 작은 값과 피벗값 교체
            if left > right:
                array[right], array[pivot] = array[pivot], array[right]
    				#엇갈리지 않았다면 작은 값과 큰 값을 교체
            else:
                array[left], array[right] = array[right], array[left]

        # 분할 이후 왼쪽과 오른쪽에서 각각 정렬 수행
        quick_sort(array, start, right - 1)
        quick_sort(array, right + 1, end)

    quick_sort(array, 0, len(array) -1)
    print(array)
    ```

  - python 2 (파이썬 장점 살린 형태) - 시간 면에선 조금 비효율적, 직관적이고 기억하기 쉬움

    ```python
    array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

    def quick_sort(array):
        # 리스트가 하나 이하의 원소만을 담고 있다면 종료
        if len(array) <= 1:
            return array

        pivot = array[0]
        tail = array[1:]

        left_side = [x for x in tail if x <= pivot] #분할된 왼쪽 부분
        right_side = [x for x in tail if x > pivot] #분할된 오른쪽 부분

        # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬을 수행하고, 전체 리스트를 반환
        return quick_sort(left_side) + [pivot] + quick_sort(right_side)

    print(quick_sort(array))
    ```

## **계수 정렬**

: 데이터 크기 범위가 제한되어 정수 형태로 표현할 수 있을 때만 사용 가능한 매우 빠른 정렬 알고리즘

동일한 값 가지는 데이터가 여러 개 등장할 때 적합. (데이터 크기 중복 多)

일반적으로 가장 큰 데이터와 가장 작은 데이터 차이가 1,000,000 넘지 않을 때 효과적 사용 가능
(모든 범위를 담을 수 있는 크기의 리스트(배열)을 선언해야 하기 때문)

리스트의 모든 데이터가 0이 되도록 초기화한 후 데이터를 하나식 확인하며 데이터 값과 동일한 인덱스를 1씩 증가시킴. → 각 데이터가 몇 번 등장했는지 횟수 기록됨. = 정렬됨.

시간 복잡도 $`O(N+K)`$ (K는 데이터 중 최대값 크기)
앞에서부터 데이터 하나식 확인하며 인덱스 값 증가시킬 뿐만 아니라, 추후 리스트의 각 인덱스에 해당하는 값 확인 시 데이터 중 최댓값 크기만큼 반복 수행해야 하기 때문.

- 코드

  ```python
  # 모든 원소의 값이 0보다 크거나 같다고 가정
  array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]
  # 모든 범위 포함하는 리스트 선언 (모든 값 0으로 초기화)
  count = [0]*(max(array) + 1)

  for i in range(len(array)):
      count[array[i]] += 1 # 각 데이터에 해당하는 인덱스의 값 증가

  for i in range(len(count)): #리스트에 기록된 정렬 정보 확인
      for j in range(count[i]):
          print(i, end=' ') #띄어쓰리를 구분으로 등장한 횟수만큼 인덱스 출력
  ```

## **병합 정렬**

퀵 정렬과 동작 방식 비슷. 일반적으로 퀵 정렬보다 느리지만 최악의 경우에도 시간 복잡도 $`O(NlogN)`$을 보장. - `sorted()` 함수와 `sort()` 함수

## 정렬 라이브러리

- `sorted()` 함수: 딕셔너리 자료형 등을 입력받아 정렬된 결과(리스트) 출력.
- `sort()` 함수: 별도의 정렬된 리스트 반환할 필요 없이 내부 원소가 바로 정렬.
- 둘 다 병합 정렬에 기반하지만 삽입 정렬의 아이디어를 더한 하이브리드 방식의 정렬 알고리즘 사용.
- key 매개변수를 입력받아서 할 수도 있음. key값으로는 하나의 함수가 들어가야 하며 이는 정렬 기준이 됨.

  ```python
  array = [('바나나', 2), ('사과', 5), ('당근', 3)]

  def setting(data):
      return data[1]

  result = sorted(array, key=setting)
  print(result)
  # 결과값: [('바나나', 2), ('당근', 3), ('사과', 5)]
  ```

- 정렬 알고리즘이 사용되는 경우
  1. 정렬 라이브러리로 풀 수 있는 문제: 단순히 정렬 기법 알고 있는지 물어보는 문제.
  2. 정렬 알고리즘의 원리에 대해 물어보는 문제
  3. 더 빠른 정렬이 필요한 문제: 퀵 정렬로는 불가. 계수 정렬 등의 다른 정렬 알고리즘 이용하거나 기존에 알려진 알고리즘의 구조적 개선 거쳐야 풀 수 있음

---

참고

- 이것이 취업을 위한 코딩테스트다 - 정렬
