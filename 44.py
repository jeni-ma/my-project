from itertools import combinations

def solve():
    # Read input
    n = int(input())
    letters = input().split()
    k = int(input())
    
    a_count = letters.count('a')
    not_a_count = n - a_count
    from math import comb
    total_ways = comb(n, k)
    
    ways_with_no_a = comb(not_a_count, k)
    
    prob = 1 - (ways_with_no_a / total_ways)
    
    print(f"{prob:.4f}")

if __name__ == "__main__":
    solve()
