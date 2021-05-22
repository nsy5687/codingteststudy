n, m = map(int, input().split())
x, y, direction = map(int, input().split())

d = [[0] * m for _ in range(n)]#여기서 for _ in range(n)안에 '_'의 의미는 인덱스를 무시한다는 의미이다(단순반복만 할 때 사용)
#[0] * m은 리스트안에 0을 m번만큼 넣는다는 의미이다
d[x][y] = 1

arrays = []

for i in range(n):
    arrays.append(list(map(int, input().split())))

dx = (-1, 0, 1, 0)
dy = (0, 1, 0, -1)

def left():
    global direction
    direction-=1
    if direction == -1:
        direction = 3

count = 1
turn = 0

while True:

    left()
    
    nx = x + dx[direction]
    ny = y + dy[direction]

    if d[nx][ny] == 0 and arrays[nx][ny] == 0:
        d[nx][ny] = 1
        x, y = nx, ny
        count+=1
        turn = 0
        continue
    else:
        turn+=1
    
    if turn == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]

        if arrays[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn = 0

print(count)