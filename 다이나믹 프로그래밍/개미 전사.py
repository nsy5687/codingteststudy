n = int(input())

array = list(map(int, input().split()))

d = [0] * n

d[0] = array[0]
d[1] = max(array[0], array[1])

for i in range(2, n):
    # 점화식 max(a[i-1], a[i-2] + arrays[i])
    # i-1번째 값과 i-2번째랑 i번째 값을 더한 값을 비교한다
    d[i] = max(d[i-1], d[i-2]+array[i])

print(d[n-1])
