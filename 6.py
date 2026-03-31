if __name__ == '__main__':
    n = int(raw_input())
    # Use raw_input() to get the string, then split and map
    integer_list = map(int, raw_input().split())
    
    t = tuple(integer_list)
    print hash(t)
