# for element in [1, 2, 3]:
#     print(element)

# for element in (1, 2, 3):
#     print(element)

# dict = {'one':1, 'two':2}

# for value in dict:
#     print(dict[value])

# for char in "123":
#     print(char)

# for line in open("myfile.txt")
#     print(line, end=' ')

# s = 'abc'
# it = iter(s)
# print(it)
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))


class Reverse:
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]

rev = Reverse('spam')
iter(rev)
for char in rev:
    print(char)
