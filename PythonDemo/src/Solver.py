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
print(hex(12))


def myabs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('SB')
    elif x >= 0:
        return x
    else:
        return -x


print(myabs(-10))

import math


def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


r = move(1, 1, 10, 0)
print(r)


def calc(*numbers):
    sum = 0
    for i in numbers:
        sum += i * i
    print(sum)
    return sum


calc(1, 2, 3)
calc()
a = [1, 2, 3]
calc(*a)