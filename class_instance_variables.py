# class Dog:

#     kind = 'canine' # class variable

#     def __init__(self, name):
#         self.name = name # instance variable
#         self.tricks = [] # instance variable

#     def add_trick(self, trick):
#         self.tricks.append(trick)


# d = Dog('Fido')
# e = Dog('Buddy')
# d.add_trick('roll over')
# e.add_trick('play dead')
# print(d.tricks)
# print(e.tricks)




# def f1(self, x, y):
#     return min(x, x+y)

# class C:
#     f = f1

#     def g(self):
#         return "hello world"

#     h = g

# z = C()
# print(z.f(1, 2))
# print(z.g())
# print(z.h())


class Bag:
    def __init__(self):
        self.data = []

    def add(self, x):
        self.data.append(x)

    def addtwice(self, x):
        self.add(x)
        self.add(x)

bag = Bag()
bag.add(1)
bag.addtwice(2)
print(bag.data)

