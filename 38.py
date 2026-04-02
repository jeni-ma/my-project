from collections import deque

n = int(input())
d = deque()

for _ in range(n):
    command = input().split()
    method = command[0]
    if len(command) > 1:
        getattr(d, method)(command[1])
    else:
        getattr(d, method)()

print(*(d))
