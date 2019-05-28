# def reverse(data):
#     for index in range(len(data)-1, -1, -1):
#         yield data[index]

# for char in reverse('golf'):
#     print(char)




# x = sum(i*i for i in range(10))
# print(x)



# xvec = [10, 20, 30]
# yvec = [7, 5, 3]

# z = zip(xvec, yvec)
# a = list(z)
# print(a)

# y = sum(x*y for x,y in zip(xvec, yvec))
# print(y)



# from math import pi, sin
# sine_table = {x: sin(x*pi/180) for x in range(0, 91)}
# print(sine_table)



# unique_words = set(word for line in page for word in line.split())

# valedictorian = max((student.gpa, student.name) for student in graduates)

data = 'golf'
r = list(data[i] for i in range(len(data)-1, -1, -1))
print(r)

