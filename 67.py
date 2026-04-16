import re
import sys

def solve():
    # Read number of lines
    n = int(input())
    
    for _ in range(n):
        line = input()

        def replace_logic(match):
            if match.group(0) == " && ":
                return " and "
            return " or "


        pattern = r"(?<= )(&&|\|\|)(?= )"
        

        line = re.sub(pattern, lambda x: "and" if x.group(0) == "&&" else "or", line)
        line = re.sub(pattern, lambda x: "and" if x.group(0) == "&&" else "or", line)
        
        print(line)

if __name__ == "__main__":
    solve()
