import sys
def solve():
    input_data = sys.stdin.read().split()    
    if not input_data:
        return
    n = int(input_data[0])
    m = int(input_data[1])
    array_elements = input_data[2:n+2]
    set_a = set(input_data[n+2:n+m+2])
    set_b = set(input_data[n+m+2:n+2*m+2])
    happiness = 0
    for x in array_elements:
        if x in set_a:
            happiness += 1
        elif x in set_b:
            happiness -= 1            
    print(happiness)
if __name__ == "__main__":
    solve()
