n = int(input())
data = input().split()

x, y = 1, 1

type = ['R','L','U','D']
dy = [1,-1,0,0]
dx = [0,0,-1,1]


for i in data:
    for j in range(len(type)):
        if i == type[j]:
            vx = x + dx[j] #여기서 vx와 vy는 전역변수이다
            vy = y + dy[j] #전역변수랑 지역변수는 함수에서만 구분을 한다(명령문안에서 선언한다고 지역변수는 아님)
    if vx < 1 or vx > n or vy < 1 or vy > n:
        continue
    else:
        x, y = vx, vy

print(x, y)