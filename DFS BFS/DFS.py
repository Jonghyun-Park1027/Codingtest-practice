# 시간초과(노드부터 못만듦)
'''
n, m = map(int,input().split())

map_size = []
for _ in range(n):
    map_size.append(list(map(int,input())))


# print(n, m , map_size)

def dfs(x,y):
    if x <= -1 or x>=n

'''
'''
# N, M을 공백을 기준으로 구분하여 입력 받기
n, m = map(int, input().split())

# 2차원 리스트의 맵 정보 입력 받기
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# DFS로 특정한 노드를 방문한 뒤에 연결된 모든 노드들도 방문
def dfs(x, y):
    # 주어진 범위를 벗어나는 경우에는 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 0:
        # 해당 노드 방문 처리
        graph[x][y] = 1
        # 상, 하, 좌, 우의 위치들도 모두 재귀적으로 호출
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False

# 모든 노드(위치)에 대하여 음료수 채우기
result = 0
for i in range(n):
    for j in range(m):
        # 현재 위치에서 DFS 수행
        if dfs(i, j) == True:
            result += 1

print(result) # 정답 출력
'''
'''
4 5
00110
00011
11111
00000
'''
n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int,list(input()))))

def dfs(graph,n,m):
    graph[n][m] =1
    try :
        if graph[n-1][m] == 0 :
            dfs(graph,n-1,m)
            print("work1", n-1,m)
        if graph[n+1][m] == 0:
            dfs(graph,n+1, m)
            print("work2",n+1,m)
        if graph[n][m-1] == 0:
            dfs(graph, n, m-1)
            print("work3",n,m-1)
        if graph[n][m+1] == 0:
            dfs(graph, n, m+1)
            print("work4",n,m+1)
    except :
        return
    return graph

a =dfs(graph, 0,0)
print(a)
#
#
# for i in graph:
#     for j in i:
#         if j == 0:
#             graph[i][j] = 1
#             if j+1 == 0:
#                 graph[i][j+1] = 1
#             if j-1 == 0:
#                 graph[]

# visited = [[False] * m] * n

# print(visited)