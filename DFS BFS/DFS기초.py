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

def dfs(graph,i,visied):
    visied[i] = True #방문시 체크

    print(i, end=' ') #방문 된 노드를 출력 

    for j in graph[i]: #현재 노드와 연결 된 노드들을 차례로 확인하면서 방문하지 않은 노드가 존재시 재귀함수를 통해 방문
        if not visied[j]:
            dfs(graph,j,visied)#재귀함수는 스택역할을 한다(과정이 거의 비슷하다)

dfs(graph,1,visied)
