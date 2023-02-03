N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, list(input()))))
count = 0


def dfs(graph, n, m):
    global N, M
    if n >= N and m >= M:
        return
    graph[n][m] = 1

    # up
    if n - 1 > -1 and graph[n - 1][m] == 0:
        dfs(graph, n - 1, m)
    # down
    if n + 1 < N and graph[n + 1][m] == 0:
        dfs(graph, n + 1, m)
    # left
    if m - 1 > -1 and graph[n][m - 1] == 0:
        dfs(graph, n, m - 1)
    # right
    if m + 1 < M and graph[n][m + 1] == 0:
        dfs(graph, n, m + 1)

    return


# find '0'
for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            dfs(graph, i, j)
            count += 1

print(count)
