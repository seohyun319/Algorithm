# C6. 정렬 - 실전문제 '성적이 낮은 순서대로 학생 출력하기'

n = int(input())
array = []
for i in range(n):    
    name, score = input().split() #원래 map으로 하려고 했는데 둘 다 int형인 게 아니라서 그냥 입력 받음
    array.append((name, int(score))) #append는 입력값 하나만 받기 때문에 튜플형 세트로 보려면 ()로 묶어야 함. 

# 두 번째 값인 성적을 기준값으로 정렬할 수 있도록 성적값 리턴
def make_key(put):
    return put[1]

array = sorted(array, key=make_key) #키 값 기준 정렬
#함수 lambda로 만들면 
#array = sorted(array, key=lambda student: student[1])
#로 하고 밑에 for문에서 student[0] 프린트하면 됨.

for i in range(n):
    print(array[i][0], end=' ') #array[i][0]은 이름, array[i][1]은 성적

