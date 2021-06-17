import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())


start = int(input())

#그래프 크기지정
graph = [[] for _ in range(n + 1)]
#거리랑 방문체크 리스트
visited = [False] * (n + 1)
distance = [INF] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))

#모든 노드 중 방문을 하지 않고 거리가 짧을 노드의 인덱스 값을 반환해주는 함수
def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1, n + 1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):

    #시작노드의 거리를 0으로 지정, 방문처리를 해준다
    distance[start] = 0
    visited[start] = True

    #시작노드와 연결 된 노드들의 거리를 거리리스트에 업데이트
    for j in graph[start]:
        distance[j[0]] = j[1]

    #그 외 거리가 짧은 노드부터 처리하며서 반복
    for i in range(n - 1):
        #거리가 짧은 노드의 인덱스를 now변수에 초기화, now위치의 노드를 방문처리한다
        now = get_smallest_node()
        visited[now] = True

        #현재 노드의 거리랑 연결 된 노드의 거리를 더하고 연결 된 노드의 거리랑 비교하여 짧은 노드이면 거리리스트에 업데이트
        for j in graph[now]:
            cost = distance[now] + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost

dijkstra(start)

for i in range(1, n + 1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])
