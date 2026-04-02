from collections import deque

def can_stack(cubes):
    d = deque(cubes)
    last_picked = float('inf')
    
    while d:
        # Pick the larger of the two ends
        if d[0] >= d[-1]:
            current = d.popleft()
        else:
            current = d.pop()
        if current > last_picked:
            return "No"        
        last_picked = current        
    return "Yes"
t = int(input())
for _ in range(t):
    n = int(input())
    side_lengths = list(map(int, input().split()))
    print(can_stack(side_lengths))
