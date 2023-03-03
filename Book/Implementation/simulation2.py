'''# %%
n, m = map(int, input().split())
# A는 북쪽으로부터 떨어진 칸의 개수, 즉 row(n), B는 서쪽으로부터 떨이잔 개수 column(m)
position_x, position_y, direction = map(int, input().split())
map_size = []
count = 0
visit = []
for _ in range(n):
    map_size.append(list(map(int, input().split())))
# print(map_size)
# 방향은 0:북, 1동, 2남, 3서
# 1. 현재 위치 기준으로 왼쪽방향
# print(map_size[position_x][position_y])
while True:
    visit_list = [position_x, position_y]
    # print(visit_list)
    direct_count = 0
    if direction == 0:
        if map_size[position_x - 1][position_y] == 1:
            direction = 3
            direct_count += 1
        elif map_size[position_x - 1][position_y] == 0:
            position_x -= 1
            if visit_list not in visit:
                visit.append(visit_list)
                count += 1
                # print(visit_list)
            elif visit_list in visit:
                # print("a")
                direction = 3
                direct_count += 1
    # print(direction, position_x)
    if direction == 3:
        if map_size[position_x][position_y - 1] == 1:
            direct_count += 1
            direction = 2
        elif map_size[position_x][position_y - 1] == 0:
            position_y -= 1
            if visit_list not in visit:
                visit.append(visit_list)
                count += 1
            elif visit_list in visit:
                direction = 2
                direct_count += 1

    if direction == 2:
        if map_size[position_x + 1][position_y] == 1:
            direct_count += 1
            direction = 1
        elif map_size[position_x + 1][position_y] == 0:
            position_x += 1
            if visit_list not in visit:
                visit.append(visit_list)
                count += 1
            elif visit_list in visit:
                direct_count += 1
                direction = 1
    if direction == 1:
        if map_size[position_x][position_y + 1] == 1:
            direct_count += 1
            direction = 0
        elif map_size[position_x][position_y + 1] == 0:
            position_y += 1
            if visit_list not in visit:
                visit.append(visit_list)
                count += 1
            elif visit_list in visit:
                direct_count += 1

                direction = 0
    if direct_count == 4:
        break
# if map_size[position_x-1][]
print(position_x, position_y, direction, count, visit)

'''
# 정답
# N, M을 공백을 기준으로 구분하여 입력받기
n, m = map(int, input().split())

# 방문한 위치를 저장하기 위한 맵을 생성하여 0으로 초기화
d = [[0] * m for _ in range(n)]
# 현재 캐릭터의 X 좌표, Y 좌표, 방향을 입력받기
x, y, direction = map(int, input().split())
d[x][y] = 1 # 현재 좌표 방문 처리

# 전체 맵 정보를 입력받기
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

# 북, 동, 남, 서 방향 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽으로 회전
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

# 시뮬레이션 시작
count = 1
turn_time = 0
while True:
    # 왼쪽으로 회전
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    # 회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    # 회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
    else:
        turn_time += 1
    # 네 방향 모두 갈 수 없는 경우
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        # 뒤로 갈 수 있다면 이동하기
        if array[nx][ny] == 0:
            x = nx
            y = ny
        # 뒤가 바다로 막혀있는 경우
        else:
            break
        turn_time = 0

# 정답 출력
print(count)