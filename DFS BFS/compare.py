N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, list(input()))))
count = 0
def dfs(graph,n,m):
    global N, M, count
    if n >= N and m >= M:
        print("enough")
        return
    print(n,m)
    graph[n][m] = 1



    #up
    if n-1 > -1 and graph[n-1][m] == 0:
        print("up",graph)
        dfs(graph, n-1, m)
    #down
    if n+1 < N and graph[n+1][m] == 0:
        print("down", graph)
        dfs(graph, n+1, m)
    #left
    if m-1 > -1 and graph[n][m-1] == 0:
        print("left", graph)
        dfs(graph, n, m-1)
    #right
    if m+1 < M and graph[n][m+1] == 0:
        print("right", graph)
        dfs(graph, n, m+1)
    print("count", count)
    count += 1
    return
#find '0'
for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            dfs(graph,i,j)

print(count)
