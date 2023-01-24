# 실패
n, m, v = map(int, input(), split())
graph = []
for _ in range(m):
    graph.append(list(map(int, input(), split())))
# DFS
visited = [False] * n
stack = []


def DFS(x, y):
    stack.append([x, y])


for i in graph:

    for j in i:
        if visited[j - 1] != True:
            visited[j - 1] = True
