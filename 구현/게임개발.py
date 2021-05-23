n, m = map(int, input().split())
x, y, direction = map(int, input().split())

#방문한 위치를 표시하기 위해 0으로 초기화
d = [[0] * m for _ in range(n)]#여기서 for _ in range(n)안에 '_'의 의미는 인덱스를 무시한다는 의미이다(단순반복만 할 때 사용)
#[0] * m은 리스트안에 0을 m번만큼 넣는다는 의미이다
d[x][y] = 1#시작시 방문체크

arrays = []

for i in range(n):
    arrays.append(list(map(int, input().split())))

dx = (-1, 0, 1, 0)
dy = (0, 1, 0, -1)

#왼쪽으로 회전
def left():
    global direction
    direction-=1
    if direction == -1:
        direction = 3

count = 1
turn = 0

while True:
    #메뉴얼 1번
    left()
    
    #메뉴얼 2번
    nx = x + dx[direction]
    ny = y + dy[direction]

    if d[nx][ny] == 0 and arrays[nx][ny] == 0: #아직 가보지 않은 육지가 존재하면 이동, 체크, 방향회전 횟수 초기화를 한다
        d[nx][ny] = 1
        x, y = nx, ny
        count+=1
        turn = 0
        continue
    else: #아니면 회전횟수 1증가
        turn+=1
    
    #메뉴얼 3번
    if turn == 4: #네 방향 모두 갈 곳이 없으면
        nx = x - dx[direction]
        ny = y - dy[direction]

        if arrays[nx][ny] == 0:# 뒤로 갈 공간이 있으면 뒤로 가고 횟수 초기화
            x = nx
            y = ny
        else: #아니면 while문 종료
            break
        turn = 0

print(count)