# squares = []
# for x in range(10):
#     squares.append(x**2)

# print(squares)

# squares = list(map(lambda x: x**2 range(10)))


# list comprehension

# squares = [x**2 for x in range(10)]
# print(squares)


# combo = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
# print(combo)

# is the same as:

# combs = []
# for x in [1, 2, 3]:
#     for y in [3, 1, 4]:
#         if x != y:
#             combs.append((x, y))

# print(combs)

# vec = [-4, -2, 0, 2, 4]
# vec_doubles = [x*2 for x in vec]
# print(vec_doubles)

# vec_positives = [x for x in vec if x >= 0]
# print(vec_positives)

# vec_absolutes = [abs(x) for x in vec]
# print(vec_absolutes)

# freshfruit = [' banana', '   loganberry ', 'passion fruit   ']
# freshfruit_stripped = [fruit.strip() for fruit in freshfruit]
# print(freshfruit_stripped)

# num_and_square = [(x, x**2) for x in range(1, 6)]
# print(num_and_square)

# tuple must be parenthesized or else an error is raised

# num_and_square = [x, x**2 for x in range(1, 6)]
# print(num_and_square)

# vec = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# vec_flat = [num for elem in vec for num in elem]
# print(vec_flat)

from math import pi
pi_round = [str(round(pi, i)) for i in range(1, 6)]
[print(num) for num in pi_round]
