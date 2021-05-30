n = int(input())
array = set(map(int,input().split()))
#집합자료형은 값들의 모임을 말하며, 순서랑 키값이 존재하지 않고 append같은 함수를 사용할 수 없다
#set(원소들)

m = int(input())
x = list(map(int,input().split()))

for i in x:
    if i in array:
        print('yes', end = ' ')
    else:
        print('no', end = ' ')