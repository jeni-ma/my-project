import re
import sys

def check_regex():
    try:
        line = sys.stdin.readline()
        if not line:
            return
        t = int(line.strip())
        for _ in range(t):
            s = sys.stdin.readline().strip()
            try:
                re.compile(s)
                print(True)
            except re.error:
                print(False)
    except ValueError:
        pass

if __name__ == '__main__':
    check_regex()
