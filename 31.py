if __name__ == '__main__':
    m = int(input())
    set_a = set(map(int, input().split()))
    n = int(input())
    set_b = set(map(int, input().split()))
    
    res = sorted(set_a.symmetric_difference(set_b))
    
    for i in res:
        print(i)