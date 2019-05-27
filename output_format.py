# s = "Hello, world."
# print(str(s))
# print(repr(s))

# print(str(1/7))

# x = 10 * 3.25
# y = 200 * 200
# s = "The value of x is " + repr(x) + ", and y is " + repr(y) + "..."
# print(s)

# hello = 'hello, world\n'
# print(hello)
# hellos = repr(hello)
# print(hellos)

# an_object = repr((x, y, ('spam', 'eggs')))
# print(an_object)




# for x in range(1, 11):
#     print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
#     print(repr(x*x*x).rjust(4))

# for x in range(1, 11):
#     print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))



# x = '12'.zfill(5)
# print(x)
# y = '-3.14'.zfill(7)
# print(y)
# z = '3.14159265359'.zfill(5)
# print(z)




# print('{} doesn\'t claim to be anything other than "{}."'.format("He", "lemons"))
# print("This {food} tastes {phrase}!".format(food="lemon", phrase="sour"))
# print('{0} and {1}'.format('hello', 'goodbye'))
# print('{1} and {0}'.format('hello', 'goodbye'))
# print('This is a {0} all about how my {1} got turned {state}.'.format('story', 'life', state='upside-down'))



# contents = 'eels'
# print('My hovercraft is full of {}.'.format(contents))
# print('My hovercraft is full of {!r}.'.format(contents))


# import math
# print('The value of PI is approximately {0:.3f}'.format(math.pi))




# table = {'One': 2837, 'Two': 8324, 'Three': 3847}
# for name, phone in table.items():
#     print('{0:10} ==> {1:10d}'.format(name, phone))


table = {'One': 2837, 'Two': 8324, 'Three': 3847}
print('Two: {0[Two]:d}; One: {0[One]:d}; '
      'Three: {0[Three]:d}'.format(table))

table = {'One': 2837, 'Two': 8324, 'Three': 3847}
print('Two: {Two:d}; One: {One:d}; '
      'Three: {Three:d}'.format(**table))

print(vars())


