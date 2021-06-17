import heapq
import sys
input = sys.stdin.readline
inf = int(1e9)

n, m, c = map(int, input().split())

graph = [[] for i in range(n + 1)]
distance = [inf] * (n + 1)

for i in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))

def daikjstra(start):
    distance[start] = 0
    q = []

    heapq.heappush(q,(0, start))

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, [cost, i[0]])

daikjstra(c)


max_value = 0
count = 0

# 연결이 되어 있으면 카운트, 최대 값 비교
for i in distance:
    if i != inf:
        count += 1
        max_value = max(max_value, i)

# 여기서 count - 1을 하는 이유는 시작지점도 카운터가 되어있기 때문에 제거한다
print(count-1,max_value)


