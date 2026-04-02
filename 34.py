
n = int(input())


distinct_stamps = set()

for _ in range(n):
    stamp = input()
    distinct_stamps.add(stamp)


print(len(distinct_stamps))
