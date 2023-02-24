'''
x = int(input())
# x % 5 == 0
count = 0
def cal(x):
    global count
    if x <= 1:
        return
    if x % 5 ==0:
        print(x, "5")
        count += 1
        cal(x/5)
        # print("1")
    # x %3 == 0
    elif x % 3 ==0:
        print(x,"3")
        cal(x/3)
        # print("2")
    # x % 2 == 0
    elif x% 2 == 0:
        print(x, "2")
        cal(x/2)
    # x -1
    if (x -1) % 5 ==0 or (x-1) % 3 == 0 or (x-1) % 2 == 0:
        print(x, "1")
        cal(x-1)
# print(count)
cal(x)
print(count)
'''
# day 21
'''
# 이해가 되질 않는다...
x = int(input())
cal = []


def five(x):
    a = x // 5
    # cal.append(a)
    return a
def three(x):
    a = x // 3
    # cal.append(a)
    return a
def two(x):
    a = x //2
    # cal.append(a)
    return a
def one(x):
    a = x-1
    # cal.append(a)
    return a


def make_1(x):
    if x == 1:
        return
    data = []
    if x%5 ==0:
        num = x // 5
        data.append(num)
    if x%3 == 0:
        num = x // 3
        data.append(num)
    if x%2 == 0:
        num = x // 2
        data.append(num)
    else :
        num = x // 1
        data.append(num)
    cal.append(data)
    for i in data:
        make_1(i)
        # if cal][-1]== cal][-1]:
        #     pass
    # for in cal:
    #     if[-1] == 1:
    #         return
    #     if == False:
    #         pass
    #     make_1[-1])

# for in range(4):

make_1(x)
print(cal)
'''
# day 22
