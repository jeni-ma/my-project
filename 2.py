if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    # Remove duplicates with set(), sort them, and pick the second to last
    unique_scores = sorted(set(arr))
    print(unique_scores[-2])