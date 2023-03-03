from collections import deque
'''
data = [1,2,3,4,5]

print(data)

data_deque = deque(data)
data_deque.rotate(-1)
print(data_deque)
'''
'''
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
    if target.index(underside) == 0 or target.index(underside) == 5:

        upperside = 6
    else :
        upperside = 2
    print(f"upper index counter is {upperside}")
    # 주사위 돌려서 최대 옆면 찾기
    while True:
        # global upperside
        target.rotate(-1)
        count += 1
        # print(count)
        if count == 7:
            break
        if count == 1:
            continue
        print(target, "target work")
        if count == upperside:
            next = target[0]
            print( f"take {next} understate and back")
            continue
        if maxnum < target[0]:
            # if count == upperside:
            #     print(target[0], "back")
            #     continue

            maxnum = target[0]
            print(maxnum, "take target")
            # print(maxnum)
        # target.rotate(1)
        # print(target)
        # if count == 6:
        #     break


    data[select] += maxnum
    print(f"{data[select]} is {select}st dice max")
    select += 1
    if select == n:
        return target, data,upperside
    return start_position(next)
print(start_position(4))
print(sum(data))
'''
'''
치명적인 실수를 했는데, 그것은 리스트 rotation을 통해 구현하려 했던 아이디어 자체였다
구현자체는 성공했다 그러나 인덱스가 3 이상일 경우 -1로 이하일경우 1로 돌려야 한다는 문제가 있다
그래서 균일한 알고리즘을 구현할 수 없었고 구현방법의 실패였기에 여기서 마무리 한다.
'''
