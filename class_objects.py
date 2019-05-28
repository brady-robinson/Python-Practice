class MyClass:
    z = 12345

    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

    def f(self):
        return 'hello world'

# print(MyClass.z)
# print(MyClass.f)

x = MyClass(3.0, -4.5)
print(x.r, x.i)

x.counter = 1
while x.counter < 10:
    x.counter = x.counter * 2
print(x.counter)
del x.counter

# xf = x.f
# count = 1
# while count < 10:
#     print(xf())
#     count = count + 1

print(MyClass.f(x))