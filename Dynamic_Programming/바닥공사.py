'''
n = int(input())

graph = [[0] * n for _ in range(2)]


# cover 1 (1 X 2)
def cover_1(graph, i, j):
    for i in range(i, i+2):
        graph[0][i] += 1


# cover 2 (2 X 1)


# cover 3 (2 X 2)

num = [0] * 1001
# DP : 안에 타고들어가고 타고들어가고 타고들어가고..?
def dp(graph, i, j):
    # if sum(graph) % (2*n) == 0:
    #     return

    if graph[i][j] != 0:
        return
    cover_3(graph,i,j)

dp(graph,0, 0)

# for i in
# graph[0][2] = 1
print(graph[0])
# print(list(range(2)))
'''