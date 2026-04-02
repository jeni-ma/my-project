from itertools import combinations

if __name__ == '__main__':
    s, n = input().split()
    s = sorted(s)
    n = int(n)
    
    for i in range(1, n + 1):
        for combo in combinations(s, i):
            print("".join(combo))
