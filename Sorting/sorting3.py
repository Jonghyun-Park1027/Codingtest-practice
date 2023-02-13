'''
5 3
1 2 5 4 3
5 5 6 6 5
'''
N, K = map(int, input().split())
# print(N, K)
data = []
for _ in range(2):
    data.append(list(map(int,list(input().split()))))
A = sorted(data[0])
B = sorted(data[1], reverse=True)
# print(A,B)
count = 0
for i in range(N):
    if A[i] < B[i]:
        A[i], B[i] = B[i], A[i],
        count += 1
        if count == K:
            break
print(sum(A), B)


