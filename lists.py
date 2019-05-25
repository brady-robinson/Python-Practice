# squares = [1, 4, 9, 16, 25]
# print(squares)

# print(squares[0])
# print(squares[-3:])
# # returns a shallow copy
# print(squares[:])

# squarez = squares + [36, 49, 64, 81, 100]
# print(squarez)

cubes = [1, 8, 27, 65, 125]
print(cubes)
cubes[3] = 64
print(cubes)

cubes.append(216)
cubes.append(7 ** 3)
print(cubes)

cubes[2:4] = [1, 2, 3]
print(cubes)
cubes[2:4] = []
print(cubes)

print len(cubes)