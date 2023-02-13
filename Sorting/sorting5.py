'''
4 6
19 15 10 17
'''

n, m = map(int, input().split())
long = list(map(int,input().split()))
# for _ in range(n):
#     long.append(input())
# print(n, m, long)
longest = max(long)
ttuk = []
for _ in range(n):
    ttuk.append([0] * longest)
for i in range(n):
    for j in range(long[i]):
        ttuk[i][j] = 1
count = 0
for i in range(1,longest):
    # if sum(ttuk[0][-i:], ttuk[1][])

    # count = 0
    # print(ttuk[:][-i])
    for j in range(n):
        # count = 0
        # print("c8")
        count += ttuk[j][-i]
        # count += a
        # print(j)
        if count == m:

            print(longest - i)
            break
        # if count == m:
        #     print(i, j, count)
    #         break
        # print(i, j, count)
        # f count >= 6:
        #     break
# print(ttuk)
# print(count)