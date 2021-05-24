array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):

    #일단 첫 인덱스 값을 min_index에 저장

    min_index = i

    #각 인덱스마다 작은 값을 찾는다
    for j in range(i+1,len(array)):
        if array[min_index] > array[j]:
            min_index = j
    #첫 인덱스 값과 작은 값을 swap
    array[i], array[min_index] = array[min_index], array[i]

print(array)