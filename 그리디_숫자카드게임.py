n, m = map(int,input().split())

result=0
#min()함수만 이용--------
for i in range(n):
    data = list(map(int, input().split()))

    min_value = min(data)

    result=max(result,min_value)

print(result)

#2중for문 이용--------------

result = 0

for i in range(n):
    data = list(map(int, input().split()))

    min_value = 10000
    for j in data:
        min_value = min(min_value,j)
    
    result=max(result,min_value)

print(result)