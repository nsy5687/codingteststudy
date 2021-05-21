n, m = map(int,input().split())

result=0
#min()함수만 이용--------
for i in range(n):
    data = list(map(int, input().split()))

    min_value = min(data)#min(리스트) : 리스트 전체의 대상으로 각 항목마다 최소 값을 구한다

    result=max(result,min_value)#max(이전 비교할 숫자, 현재 비교할 숫자)

print(result)

#2중for문 이용--------------

result = 0

for i in range(n):
    data = list(map(int, input().split()))

    min_value = 10000
    for j in data:
        min_value = min(min_value,j)#min(이전 비교할 숫자, 현재 비교할 숫자)
    
    result=max(result,min_value)

print(result)