# the below example uses a lambda expression to return a function

# def make_incrementor(n):
#     return lambda x: x + n

# f = make_incrementor(42)
# print(f(0))
# print(f(1))


# the below example passes a small argument as a function

pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[1])
print(pairs)