matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

# transpose rows and columns

# option 1

matrix_transpose = [[row[i] for row in matrix] for i in range(4)]

# option 2

# transposed = []
# for i in range(4):
#     transposed.append([row[i] for row in matrix])

# print(transposed)

# option 3

# transposed = []
# for i in range(4):
#     transposed_row = []
#     for row in matrix:
#         transposed_row.append(row[i])
#     transposed.append(transposed_row)

# print(transposed)

# option 4

print(list(zip(*matrix)))
