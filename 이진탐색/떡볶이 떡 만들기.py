n, m = map(int, input().split())
array = list(map(int,input().split()))

start = 0
end = max(array) #떡들 중에 가장 긴 떡을 기준으로 결정한다


result = 0

while start <= end:
    mid = (start + end) // 2
    total = 0

    #절단기 높이(mid)보다 긴 떡이면 1씩 증가
    for i in array:
        if mid < i:
            total += i - mid
    
    #정한 길이보다 짧으면 end를 감소
    if total < m:
        end = mid - 1
    #같거나 길면 조건에 만족하기 때문에 result변수에 mid값을 넣는다
    else:
        result = mid
        start = mid + 1
        

print(result)