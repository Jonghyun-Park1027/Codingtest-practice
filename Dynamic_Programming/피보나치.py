# top-down

# 리스트 초기화(저장을 위함)
graph = [0] * 101


def pivo(x):
    # 위에서 아래로 주니까
    if graph[x] != 0:
        return graph[x]
    if x == 1 or x == 2:
        return 1
    # pivo는 점화식 n[x] = n[x-1] + n[x-2]의 법칙을 따름
    graph[x] = pivo(x - 1) + pivo(x - 2)
    return graph[x]


pivo(100)
print(graph)

# bottom-up

graph_2 = [0] * 101

graph_2[0] = 1
graph_2[1] = 1

for i in range(2, len(graph_2)):
    test = graph[i-1] + graph[i-2]
    graph_2[i] = test

print(graph_2, len(graph_2))

