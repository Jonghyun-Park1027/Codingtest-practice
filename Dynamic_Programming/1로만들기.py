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