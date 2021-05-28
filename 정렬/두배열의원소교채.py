n, k = map(int,input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort() #오름차순으로 정렬
b.sort(reverse=True) #내림차순으로 정렬

#k번까지 a[i]와 b[i]를 교체 
for i in range(k):
    #b[i]가 더 크면 교환
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
    #아니면 중단한다
    else:
        break

#a리스트안에 모든 원소를 더해 출력
print(sum(a))


