basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)

print('orange' in basket)
print('crabgrass' in basket)

a = set('abracadabra')
b = set('alacazam')
print(a)
c = a - b
print(c)
d = a | b
print(d)
e = a & b
print(e)
f = a ^ b
print(f)

# set comprehensions

x = {x for x in 'abacadabra' if x not in 'abc'}
print(x)