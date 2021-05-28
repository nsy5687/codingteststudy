n = int(input())

array = []

for i in range(n):
    data = input().split()

    array.append((data[0], int(data[1])))
#점수를 기준으로 정렬
result = sorted(array, key= lambda x : x[1])

for i in result:
    print(i[0], end=' ')