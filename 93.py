from itertools import permutations
S, k = input().split()
k = int(k)
sorted_S = sorted(S)
result = list(permutations(sorted_S, k))
for p in result:
    print("".join(p))
