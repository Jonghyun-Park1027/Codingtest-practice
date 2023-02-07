'''
2
홍길동 95
이순신 77
'''

N = int(input())
data = []
for _ in range(N):
    data.append(input().split())
dictionary = dict(data)
sorted_by_value = dict(sorted(dictionary.items(), key = lambda x: x[1]))
sorted_name = [i for i in sorted_by_value.keys()]
print(*sorted_name)