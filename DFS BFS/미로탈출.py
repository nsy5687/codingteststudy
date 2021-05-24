from collections import deque

n, m = map(int, input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

graph = []

for i in range(n):
    graph.append(list(map(int, input())))


def bfs(x, y):
    #큐 생성
    queue = deque()

    #시작 노드의 좌표를 큐에 push
    queue.append((x,y))

    #큐가 비어 있기 전까지 진행
    while queue:
        #pop을 한 후 연결 된 노드들을 큐에 넣으면서 넣은 노드들의 값을 pop한 노드값 + 1 증가
        x, y = queue.popleft()

        #4방향을 확인한다
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            #범위 외면 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            #벽이면 무시
            if graph[nx][ny] == 0:
                continue
            #한번도 방문을 하지 않았으면
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1#pop한 노드값 + 1 증가
                queue.append((nx,ny)) #push한다

    return graph[n-1][m-1]

print(bfs(0,0))


