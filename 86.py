

import numpy

n, m = map(int, input().split())

matrix = []
for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)


my_array = numpy.array(matrix)


print(numpy.transpose(my_array))

print(my_array.flatten())
