import re
import email.utils

n = int(input())
pattern = r'^[a-z][a-z0-9\._-]*@[a-z]+\.[a-z]{1,3}$'

for _ in range(n):
    name, addr = email.utils.parseaddr(input())
    if re.match(pattern, addr, re.IGNORECASE):
        print(email.utils.formataddr((name, addr)))
