import re

x = re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')
print(x)

y = re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat')
print(y)

z = 'tea for two'
t = z.replace('too', 'two')
print(t)