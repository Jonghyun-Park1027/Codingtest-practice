from collections import deque

N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, list(input()))))
way = deque()

count = 0
def bfs(graph, n, m):
    global count
    graph[n][m] = 0
    way.append([n, m])
    # print(start, start[0], start[1])
    start = way.popleft()
    # if n == N-1 and m == M-1:
    #     return
    print("start",start)
    up = start[0] - 1
    down = start[0] + 1
    left = start[1] - 1
    right = start[1] + 1
    count += 1
    while n <= N-1 and m <= M-1:
        # if n >= N-1 and m>=M-1 and n>0 and m >0:
        #     return graph,way, count

        # up
        if up >= 0 and graph[up][m] == 1:
            # way.append([up, m])
            print("up", up, m)
            bfs(graph, up, m)
        # down
        if down <= N-1 and graph[down][m] == 1:
            # way.append([down, m])
            print("down",down, m)
            bfs(graph, down, m)
        # left
        if left >= 0 and graph[n][left] == 1:
            # way.append([n, left])
            print("left",n,left)
            bfs(graph, n, left)
        # right
        if right <= M-1 and graph[n][right] == 1:
            # way.append([n, right])
            print("right",n, right)
            bfs(graph, n, right)
        if n >= N-1 and m >= M-1:
            print("end")
        return graph, way, count


a = bfs(graph, 0, 0)

print(a)
