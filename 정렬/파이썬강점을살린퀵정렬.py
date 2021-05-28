array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

#퀵 정렬은 피벗을 중심으로 왼쪽은 작은 값 오른쪽은 큰 값으로 정렬되어있는 특징을 가지고 있다
#이 소스파일에서는 파이썬의 장점과 퀵 정렬의 특징을 이용하여 작성하였다

def quick(array):
    #원소 객수가 1개면 종료
    if len(array) <= 1:
        return array

    pivot = array[0] #첫 번째 원소를 피벗으로 지정
    tail = array[1:] #나머지를 tail에 넣는다

    left = [x for x in tail if x <= pivot] #피벗보다 작으면 left
    right = [x for x in tail if x > pivot] #피벗보다 크면 right

    return quick(left) + [pivot] + quick(right) # 재귀함수를 통해 정렬을 하고 리턴한다

quick(array)

print(quick(array))

