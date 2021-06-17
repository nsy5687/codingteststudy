# 플로이드 워셜 알고리즘은 모든 지점에서 다른 모든 지점까지의 최단 경로를 모두 구해야 하는 겅우에 사용할 수 있는 알고리즘이다.
# 총시간 복잡도는 O(N^3)이다
# 최단 경로의 공식은 k번째일때 d[a][b] = min(d[a][b], d[a][k] + d[k][b])

inf = int(1e9)

graph = [
    [0,4,inf,6],
    [3,0,7,inf],
    [5,inf,0,4],
    [inf,inf,2,0]
]

for k in range(len(graph)):
    for a in range(len(graph)):
        for b in range(len(graph[a])):
            graph[a][b] = min(graph[a][b],graph[a][k]+graph[k][b])

for i in range(len(graph)):
    for j in range(len(graph[i])):
        print(graph[i][j], end=" ")
    print()