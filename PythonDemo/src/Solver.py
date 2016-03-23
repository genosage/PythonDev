print("Tom", 'and'.capitalize(), "Jerry")
# print(input('Test Input: \n'))
print("I'm \"\n\\leaving")
print("\\\t\\")
print(r"\\\t\\")
print('''ha
haha
hahaha''')
print(ord("抽"))
print(chr(25591))
print('bytes'.encode('ascii'))
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))
print(len("csapp"))
# list
list = ['oh', 20, 2.78]
print(list)
print(len(list), list[-3])
list.append('abc')
print(list[-1])
list.insert(2, 'first')
list.pop(1)
print(list)
s = ['python', 'java', ['asp', 'php'], 'scheme']
print(s)
# tuple
tuple = ('1', 1, 1, '1', 1)
print(tuple.count('1'))
list.extend(['ha', True])
print(list)