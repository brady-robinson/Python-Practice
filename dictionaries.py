tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
print(tel)
print(tel['jack'])

del tel['sape']
print(tel)

tel['irv'] = 4127
print(tel)

print(list(tel.keys()))

print(sorted(tel.keys()))

print('guido' in tel)
print('jack' not in tel)

tel2 = dict([('jack', 3424), ('guido', 8493), ('sape', 2384)])
print(tel2)

new_dictionary = {x: x**2 for x in (2, 4, 6)}
print(new_dictionary)