# %%
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