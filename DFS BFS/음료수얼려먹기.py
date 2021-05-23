n, m = map(int, input().split())

graph = []

for i in range(n):
    graph.append(list(map(int, input())))

def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= m: #범위 밖이면 False값 반환

        return False

    if  graph[x][y] == 0: #방문을 하지 않았으면

        graph[x][y] = 1 #체크를 하고

        #각 방향마다 확인을 하고

        dfs(x+1,y)
        dfs(x-1,y)
        dfs(x,y+1)
        dfs(x,y-1)
    
        return True #True 값 반환

    return False #아니면 False값 반환

count = 0

#전부 돌면서 얼음이 몇개있는지 확인한다

for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            count += 1

print(count)