from collections import deque

visied = [False] * 9

graph =[ #인접 행렬 노드를 사용
    [], # 노드번호를 편한하게 관리하기위해 비어 둠
    [2,3,8],  #노드 1
    [1,7],    #노드 2
    [1,4,5],  #노드 3
    [3,5],    #노드 4
    [3,4],    #노드 5
    [7],      #노드 6
    [2,6,8],  #노드 7
    [1,7]     #노드 8
]

def bfs(graph, start, visied):#bfs는 dfs랑 다르게 큐를 이용하므로 스택대신인 재귀함수를 하지 않는다

    queue = deque([start])#큐 생성시 기본으로 시작노드를 가지고 생성된다

    visied[start] = True

    while queue: #큐가 비어질때까지 반복
        v = queue.popleft()

        print(v, end = ' ')

        for i in graph[v]: #pop이 되면서 pop된 노드에서 연결 된 노드들 중 방문하지 않은 노드들만 큐에 push한다
            if not visied[i]:
                queue.append(i)
                visied[i] = True

bfs(graph,1,visied)