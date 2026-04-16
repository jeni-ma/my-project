import re

for _ in range(int(input())):
    s = input()
    

    is_valid = bool(re.match(r'^[a-zA-Z0-9]{10}$', s))
    

    is_valid &= len(set(s)) == 10
    

    is_valid &= len(re.findall(r'[A-Z]', s)) >= 2
    

    is_valid &= len(re.findall(r'[0-9]', s)) >= 3
    
    print("Valid" if is_valid else "Invalid")
