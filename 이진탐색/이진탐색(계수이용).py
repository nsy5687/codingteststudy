n = int(input())

array = [0] * 100001

for i in input().split():
    array[int(i)] += 1 

m = int(input())

x = list(map(int, input().split()))

for i in x:
    #찾고자 하는 값이 없으면(0)이면 no을 출력
    if array[i] == 0:
        print('no', end = ' ')
    else:
        print('yes', end = ' ')
