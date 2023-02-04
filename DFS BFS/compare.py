from collections import deque

N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, list(input()))))
way = deque()


def bfs(graph, n, m):
    # global N, M
    graph[n][m] = 0
    way.append([n, m])
    # print(start, start[0], start[1])
    start = way.popleft()
    if n >= N-1 and m >= M-1:
        return graph, way
    print("start",start)
    up = start[0] - 1
    down = start[0] + 1
    left = start[1] - 1
    right = start[1] + 1
    while True:
        if n >= N-1 and m>=M-1:
            return

        # up
        # if up >= 0 and graph[up][m] == 1:
        # way.append([up, m])
        # bfs(graph, up, m)
        # down
        if down <= N and graph[down][m] == 1:
            # way.append([down, m])
            print("down",down, m)
            bfs(graph, down, m)
        # left
        # if left >= 0 and graph[n][left] == 1:
        #     # way.append([n, left])
        #     bfs(graph, n, left)
        # right
        if right <= M and graph[n][right] == 1:
            # way.append([n, right])
            print("right",n, right)
            bfs(graph, n, right)
        return graph, way


a = bfs(graph, 0, 0)

print(a)
