array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):#1에서 시작하는 이유는 0번째에는 그 자체가 정렬되어 있기 때문이다

    #i번째 값을 왼쪽으로 하나씩 비교하면서 자신보다 작은 값을 만나기 전까지 이동한다

    for j in range(i, 0, -1): #i번째부터 1번째까지 -1식 증가한다
        if array[j-1] > array[j]:
            array[j-1], array[j] = array[j], array[j-1]

        #자신보다 작은 값이 있으면 중단
        else:
            break

print(array)
