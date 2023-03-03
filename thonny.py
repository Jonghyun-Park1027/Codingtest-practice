from collections import deque
# 입력 받기
n = int(input())
graph = []
data = [0] * n
def spin(node : deque, i):
    node.rotate(-i)
    return node
for _ in range(n):
    a = list(map(int, input().split()))
    graph.append(a)
select = 0

# 재귀함수 만들기
def start_position(underside):
    global select, upperside
    # 주사위 정하기
    target = deque(graph[select])
    # 주사위의 아랫면 정하기
    count= 0
    maxnum = 0
    # 주사위의 A,B,C,D,E,F 숫자 나열 순서에 따라 윗면 정하기
    if target.index(target[underside]) == 0 or target.index(target[underside]) == 5:

        upperside = 5
    else :
        upperside = 2
        # print(upperside)
    # 주사위 돌려서 최대 옆면 찾기
    while count != 6:
        # global upperside
        count += 1
        # if
        if maxnum < target[0]:
            if count == upperside:
                print(target[0], "back")
                continue
            maxnum = target[0]
            print(maxnum)
        target.rotate(-1)
        # if count == 6:
        #     break
    data[select] += maxnum
    select += 1
    if select == n:
        return target, data, upperside
    return start_position(target[upperside])
print(start_position(0))
# print(a)
    # print(target)
# print(graph[0], target, data, upperside)
# a =spin(target, 1)
