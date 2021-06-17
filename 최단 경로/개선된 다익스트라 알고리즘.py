import heapq

inf = int(1e9)

n = 7

graph = [
    [],
    [(2,2),(3,3),(4,1)],
    [(3,3),(4,2)],
    [(2,3),(6,5)],
    [(3,3),(5,1)],
    [(3,1),(6,2),],
    [],
    ]

distance = [inf] * n

def daijkstra(start):
    # 우선순위 큐를 q리스트로 생성할때 시작노드와 거리 0을 넣는다

    q = []

    heapq.heappush(q,(0,start))
    distance[start] = 0

    #큐에 비어있지 않으면
    while q:
        #거리가 가장 짧은 노드를 꺼내어 dist, now 변수에 할당
        dist, now = heapq.heappop(q)

        #꺼낸 노드의 거리보다 현재 거리가 짧거나 같으면 무시(꺼낸 노드가 이미 방문한 상태일 때)
        if distance[now] < dist:
            continue
        
        for i in graph[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost, i[0]))

daijkstra(1)     
    
for i in range(1, n):
    if distance[i] == inf:
        print("inf")
    else:
        print(distance[i])

