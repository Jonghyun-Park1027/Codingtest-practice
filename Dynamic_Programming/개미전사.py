'''
4
1 3 1 5
'''

n = int(input())
tank = list(map(int, input().split()))
# print(tank)
memory = [0] * 100

memory[0] = tank[0]
memory[1] = max(tank[0], tank[1])

for i in range(2, n):
    memory[i] = max(memory[i -1], memory[i-2] + tank[i])

print(memory)