'''# 실패
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
'''
''' 6일차 재도전
# 다시 도전
n, m, v= map(int,input().split())
graph = [[]]
for _ in range(m):
    graph.append(list(map(int, input().split())))

# print(graph)
def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
            # print(i)

visited = [False] * 5

dfs(graph, v, visited)
# print(visited)
print(graph)
'''
n, m, v = map(int, input().split())
graph = [[]]
for _ in range(m):
    graph.append(list(map(int, input().split())))
answer = []


def dfs(graph, v, visited):
    visited[v] = True
    # print(visited.index(True))
    print(v, end=" ")
    for i in graph[v]:
        if not visited[i] :
            for j in graph:
                if i in j:
                    print("def call")
                    dfs(graph, i, visited)






visited = [False] * m

dfs(graph, v, visited)
