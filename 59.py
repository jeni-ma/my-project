def solve():
    s = input().strip()
    

    
    def sort_key(char):
        if char.islower():
            return (0, char)
        elif char.isupper():
            return (1, char)
        elif char.isdigit():
            # If digit is odd, priority 2. If even, priority 3.
            if int(char) % 2 != 0:
                return (2, char)
            else:
                return (3, char)
                

    result = sorted(s, key=sort_key)
    print("".join(result))

if __name__ == "__main__":
    solve()
