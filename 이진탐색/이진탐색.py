n = int(input())
array = list(map(int,input().split()))

m = int(input())
x = list(map(int,input().split()))

array.sort()

#재귀함수를 이용시
def binary_search(array,target,start,end):

    #찾는 값이 없으면 None을 리턴
    if start > end:
        return None

    mid = (start + end) // 2

    if target == array[mid]:
        return mid
    elif target < array[mid]:
        return binary_search(array,target,start,mid-1)
    else:
        return binary_search(array,target,mid+1,end)
    

#반목문을 사용시 코드
# while start <= end:
#     mid = (start + end) // 2

#     if target > array[mid]:
#         start=mid+1
#     elif target < array[mid]:
#         end=mid-1
#     else:
#         return mid
# return None

for i in x:
    result = binary_search(array,i,0,n-1)
    if result == None:
        print('no', end = ' ')
    else:
        print('yes', end = ' ')

