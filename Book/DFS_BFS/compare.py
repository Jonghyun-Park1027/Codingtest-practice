graph = [0] * 101

def pivo(x):
    # 위에서 아래로 주니까
    if graph[x] != 0:
        return graph[x]
    if x == 1 or x == 2:
        return 1

    # pivo는 점화식 n[x] = n[x-1] + n[x-2]의 법칙을 따름
    graph[x] = pivo(x-1) + pivo(x-2)
    # print(x)
    return x
# print(x)
pivo(5)
print(graph)
