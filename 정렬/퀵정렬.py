array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

def quick(array,start, end):
    if start >= end:#하나이하의 원소를 가지면 종료
        return

    pivat = start #피벗인덱스 값을 맨처음 인덱스값으로 지정
    left = start+1 #피벗인덱스 바로 오른쪽 인덱스값을 left
    right = end 

    while left <= right:
        while left <= end and array[pivat] >= array[left]: #인덱스 left부터 end까지 피벗보다 큰 값이 나오기 전까지 반복
            left += 1
        while right > start and  array[pivat] <= array[right]: #인덱스 right부터 start까지 피벗보다 작은 값이 나오기 전까지 반복
            right -= 1
        
        if left > right :# 서로 엇갈리면 피버값과 right값을 교환
            array[pivat], array[right] = array[right], array[pivat]

        else:#아니면 left값이랑 right값을 교환
            array[right], array[left] = array[left],  array[right]

    #피벗기준으로 왼쪽과 오른쪽을 나눈다
    #여기서 피벗 값만 바뀐거지 인덱스 값까지 바뀐것이 아니라는 점 참고
    quick(array, start, right-1) 
    quick(array, right+1, end)

quick(array, 0, len(array)-1)
print(array)