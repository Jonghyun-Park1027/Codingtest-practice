'''
from collections import deque
n, m = map(int,input().split())
graph = []
for _ in range(n):

    graph.append(list(map(int, list(input()))))
# print(n, m, graph)
# queue = deque([start])
# count = 0
visited = [[]]
def way(x,y):
    # global count
    queue = deque([graph])
    # count +=1
    graph[x][y] = 0
    if x >= n or y >= m :
        return count
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                way(i,j)
    return count
way(1,1)
print(count)
'''

# 해답을 보니 기본개념 + 책 설명만으로 이해하기 어려울 수도 있다는 생각이 듦
'''
from collections import deque

# N, M을 공백을 기준으로 구분하여 입력 받기
n, m = map(int, input().split())
# 2차원 리스트의 맵 정보 입력 받기
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# 이동할 네 가지 방향 정의 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS 소스코드 구현
def bfs(x, y):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque()
    queue.append((x, y))
    # 큐가 빌 때까지 반복하기
    while queue:
        x, y = queue.popleft()
        # 현재 위치에서 4가지 방향으로의 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로 찾기 공간을 벗어난 경우 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 벽인 경우 무시
            if graph[nx][ny] == 0:
                continue
            # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    # 가장 오른쪽 아래까지의 최단 거리 반환
    return graph[n - 1][m - 1]

# BFS를 수행한 결과 출력
print(bfs(0, 0))
'''
'''
5 6
101010
111111
000001
111111
111111

'''
'''
from collections import deque
N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int,list(input()))))
count = 0
visited = []

def dfs(graph, n, m, visited ):
    global count, N, M
    queue = deque([n,m])
    graph[n][m] = 0
    v = queue.popleft()
    print(visited)
    # count += 1
    if n >= N and m >= M:
        return
    # right
    if graph[n][m+1] == 1 and m+1
    # down
'''
'''from collections import deque

N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, list(input()))))
way = deque()
answer = []
count = 0
going = True
def bfs(graph, n, m,answer):
    global count, going
    graph[n][m] = 0
    way.append([n, m])
    # if 0<= n and 0 <= m and
    # print(start, start[0], start[1])
    start = way.popleft()
    answer.append(start)
    up = start[0] - 1
    down = start[0] + 1
    left = start[1] - 1
    right = start[1] + 1
    # try :
    #     if graph[up][m] == 0 and graph[down][m] == 0 and graph[n][left]==0 and graph[n][right] == 0:
    #         return
    # except IndexError:
    #     pass
    # print(start[1])
    # if start[0] == N-1 and start[1] == M-1:
    #     answer.append(start)
    #     return graph, start

    # print("start",start)

    if up >= 0 and up <= N-1:
        way.append([up, m])

    if down >= 0 and down <= N-1:
        way.append([down, m])
    if left >= 0 and left <= M-1:
        way.append([n, left])
    if right >= 0 and right <= M-1:
        way.append([n, right])

    while going:
        for
        bfs(graph, way[0][0], way[0][1], answer)
    # return way ,start, answer
    # count += 1
    # going = True
    # while going:
    #     # global going
    #     # if n >= N-1 and m>=M-1 and n>0 and m >0:
    #     #     return graph,way, count
    #
    #     if start[0] == N - 1 and start[1] == M - 1:
    #         # global going
    #         going = False
    #         return graph, start
    #
    #     # up
    #     if up >= 0 and graph[up][m] == 1:
    #         # way.append([up, m])
    #         print("up", up, m)
    #         bfs(graph, up, m,answer)
    #     # down
    #     if down <= N-1 and graph[down][m] == 1:
    #         # way.append([down, m])
    #         print("down",down, m)
    #         bfs(graph, down, m,answer)
    #     # left
    #     if left >= 0 and graph[n][left] == 1:
    #         # way.append([n, left])
    #         print("left",n,left)
    #         bfs(graph, n, left,answer)
    #     # right
    #     if right <= M-1 and graph[n][right] == 1:
    #         # way.append([n, right])
    #         print("right",n, right)
    #         bfs(graph, n, right,answer)
    #     # answer.append(start)
    #     # if n >= N-1 and m >= M-1:
    #     #     print("end")
    #     #     answer.append([n,m])
    #
    #     break
    # # answer.pop()

a = bfs(graph, 0, 0,answer)

# print(a)
print(way)
'''
from collections import deque

N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, list(input()))))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def dfs(x, y):
    queue = deque()
    queue.append([x, y])
    # graph[x][y] = 1
    #  상하좌우표시

    while queue:
        # queue.popleft()
        x, y = queue.popleft()
        for i in range(4):
            # 4방향 설정
            tx = x + dx[i]
            ty = y + dy[i]
            # graph를 벗어나면 지나가기
            if tx <= -1 or ty <= -1 or tx >= N or ty >= M:
                continue
            # 벽이면 지나가기
            if graph[tx][ty] == 0:
                continue
            if graph[tx][ty] == 1:
                graph[tx][ty] = graph[x][y] + 1
                queue.append([tx, ty])
    return graph[N - 1][M - 1]


a = dfs(0, 0)
print(a)
# 더하기
