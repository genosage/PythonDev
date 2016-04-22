from collections import Iterable
from functools import reduce


# print("Tom", 'and'.capitalize(), "Jerry")
# # print(input('Test Input: \n'))
# print("I'm \"\n\\leaving")
# print("\\\t\\")
# print(r"\\\t\\")
# print('''ha
# haha
# hahaha''')
# print(ord("抽"))
# print(chr(25591))
# print('bytes'.encode('ascii'))
# print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))
# print(len("csapp"))
# print('\n\n\n')
#
# # list
# list = ['oh', 20, 2.78]
# print(list)
# print(len(list), list[-3])
# list.append('abc')
# print(list[-1])
# list.insert(2, 'first')
# list.pop(1)
# print(list)
# s = ['python', 'java', ['asp', 'php'], 'scheme']
# print(s)
# print('\n\n\n')
#
# # tuple
# tuple = ('1', 1, 1, '1', 1)
# print(tuple.count('1'))
# list.extend(['ha', True])
# print(list, end='')
# print('haha')
# print('\n\n\n')

# # dict
# list = ['1', 1, 1, '1', 1]
# tuple = (1, 2, 3)
# dict = {'aaa': ['are', 'you', ('How', False)], (True, False): 'bbb', tuple: list}
# print('?' in dict)
# print(dict.get('haha', True))
# # print(dict.pop('ccc'))
# list.pop(0)
# print(dict)

# # set
# s = set([1, 2, 3])
# s.add(12)
# s.remove(1)
# print(s)
# a = [1, 3, 2]
# a.sort()
# print(a)

# function
# print(hex(12))
#
#
# def myabs(x):
#     if not isinstance(x, (int, float)):
#         raise TypeError('SB')
#     elif x >= 0:
#         return x
#     else:
#         return -x
#
#
# print(myabs(-10))
#
# import math
#
#
# def move(x, y, step, angle=0):
#     nx = x + step * math.cos(angle)
#     ny = y - step * math.sin(angle)
#     return nx, ny
#
#
# r = move(1, 1, 10)
# print(r)
#
#
# def calc(*numbers):
#     sum = 0
#     for i in numbers:
#         sum += i * i
#     print(sum)
#     return sum
#
#
# calc(1, 2, 3)
# calc()
# a = [1, 2, 3]
# calc(*a)


# def person(name, gender, **kw):
#     print('name:', name, 'gender:', gender, 'other:', kw)
#
#
# person('xiaoming', 'f', city='beijing')
# dict = {'city': 'tianjin', '12': True}
# person('xiaohong', 'm', **dict)

#
# def f(a, b, *, c, d):
#     print('a = ', a, 'b =', b, 'c =', c, 'd =', d)
#
#
# def f1(a, b, c=0, *args, **kw):
#     print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)
#
#
# def f2(a, b, c=0, *, d, **kw):
#     print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)
#
#
# f(1, 2, c=3, d=4)
# f1(1, 2, 3, 4, 5, 6, haha=8)
# f2(1, 2, 3, d=4, aa=5, sb=6)

# l = [1, 2, 3, 4, 5, 6]
# print(l[:2])
# print(l[::2])
# print(l[1:2:3])

# d = {'x': 'a', 'y': 'b', 'z': 'c'}
# print([m + ' = ' + n for m, n in d.items()])
# print(isinstance(d, dict))
#
#
# def fib(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         yield b
#         a, b = b, a + b
#         n = n + 1
#     return 'done'
#
#
# f = fib(6)
# print([i for i in f])

# print(isinstance((x for x in range(1, 10, 2)), Iterable))
#
# def add(a, b, f):
#     return f(a) + f(b)
#
# print(add(1, -2, abs))
# from setuptools.dist import sequence
#
# print(list(map(str, [1, 2, 3, 4, 5])))
#
# print(isinstance(map(abs, [1, 2, -3]), sequence))
#
# def count():
#     fs = []
#     for i in range(1, 4):
#         def f():
#              return i*i
#         fs.append(f)
#     return fs
#
# [f1, f2, f3] = count()
#
# print(f1())


# def build(x, y):
#     return lambda: x * x + y * y
#
#
# f = build(2, 3)
# print(f())
# print(f.__name__)
# print(build.__name__)
#
# class student(object):
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score
#
#     def print_score(self):
#         print('%s : %s' % (self.name, self.score))
#
# bart = student('Bart', 99)
# bart.print_score()
#
# print(type(str))

# class Student(object):
#
#     @property
#     def birth(self):
#         return self._birth
#
#     @birth.setter
#     def birth(self, value):
#         if not isinstance(value, int):
#             raise ValueError('value must be an integer!')
#         self._birth = value
#
#     @property
#     def age(self):
#         return 2016 - self._birth
#
# john = Student()
# # john.birth = 'ada'
# john.birth = 1994
# print(john.age)

class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 100000:
            raise StopIteration()
        return self.a

    def __getitem__(self, n):
        a, b = 1, 1
        for x in range(n):
            a, b = b, a + b
        return a

for i in range(10):
    print(Fib()[i])

from enum import Enum

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

