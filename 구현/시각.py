h = int(input())

count = 0
for i in range(h+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i)+ str(j) + str(k): #"str(i)+ str(j) + str(k)"안에 '3'이 하나라도 포함하면 카운터를 센다
                count += 1

print(count)

#3중for문(O(h^3))을 내가 수학적으로 풀어서 O(h)로 만들어 보았다

count=0

for i in range(h+1):
    if '3' in str(i):
        count+=3600
    else:
        count+=1575

print(count)