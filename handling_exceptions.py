# while True:
#     try:
#         x = int(input("Please enter a number: "))
#         break
#     except ValueError:
#         print("Oops! That was no valid number. Try again...")



# class C(Exception):
#     pass

# class B(C):
#     pass

# class D(C):
#     pass

# for cls in [B, C, D]:
#     try:
#         raise cls()
#     except D:
#         print("D")
#     except C:
#         print("C")
#     except B:
#         print("B")


# try:
#     raise Exception('spam', 'eggs')
# except Exception as inst:
#     print(type(inst))
#     print(inst.args)
#     print(inst)

#     x, y = inst.args
#     print('x =', x)
#     print('y =', y)


def this_fails():
    x = 1/0

try:
    this_fails()
except ZeroDivisionError as err:
    print("Handling run-time error:", err)

