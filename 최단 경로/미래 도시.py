inf = int(1e9)

n, m = map(int, input().split())

graph = [[inf] * (n + 1) for i in range(n + 1)]

for a in range(1, n + 1):
    for b in range(1, n+ 1):
        if a == b:
            graph[a][b] = 0

for i in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

x, k = map(int, input().split())

for c in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][c] + graph[c][b])

#1번 도시부터 k번 도시까지 거리 + k번 도시부터 x번 도시까지 거리
distance = graph[1][k] + graph[k][x]

if distance >= inf:
    print(-1)
else:
    print(distance)
