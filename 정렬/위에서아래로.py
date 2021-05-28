n = int(input())

array=[]

for i in range(n):
    array.append(int(input()))

#sorted함수에서 reverse=True를 통해 내림차순를 지정할 수 있다(지정을 하지 않으면 기본으로 오름차순이다)
sorted(array,reverse=True)

for i in array:
    print(i, end=' ')