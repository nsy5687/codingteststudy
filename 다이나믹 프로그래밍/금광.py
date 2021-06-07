t = int(input())

result = [0] * t

for k in range(t):
    n, m = map(int, input().split())
    array = list(map(int, input().split()))

    temp = 0
    for j in range(n):
        if temp < array[0+m*j]:
            temp = array[0+m*j]
            idx = 0+m*j
    
    result[k] = array[idx]


    for _ in range(m-1):
        
        temp = 0
        if idx - 3 > 0:
            if temp <array[idx - 3]:
                temp = array[idx - 3]
                p = idx - 3
        if idx + 1 < n*m:
            if temp <array[idx + 1]:
                temp = array[idx + 1]
                p = idx + 1
        if idx + 5 < n*m:
            if temp <array[idx + 5]:
                temp = array[idx + 5]
                p = idx + 5
        
        result[k] += temp
        idx = p
    
for i in range(t):

 
    print(result[i])