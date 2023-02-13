'''
5
8 3 7 9 2
3
5 7 9
'''
N = int(input())
have = set(map(int,list(input().split())))
M = int(input())
want = list(map(int,list(input().split())))
# print(N, have, M, want)
answer = []
for i in want:
    if i in have:
        answer.append("yes")
    else:
        answer.append("no")
print(*answer)