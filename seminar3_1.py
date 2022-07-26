# lambda - анонимные функции
# Включение - генератор list comprehension
#map  -принимает функцию с вырадением к элементу
#filtr - применяет функцию с логическим выражением к элементам
#zip - комбинирует коллекции
#enimerate - нумерует 


# f = lambda x: x**2
# print(f(20))
# def f(x):
#     return x**2
# for item in my_list:
#     print(f(item), end='')

# new_f = lambda x:x**2
# my_list = [1, 413, 65 , 346]
# res = list(map(new_f,my_list))
# print (res)


#         Чтосделать с; с кем сделать
# my_list = [ i for i in range(20)if  i > 10]

# listt = tuple([(i, i) for i in range(1, 21) if (i % 2 == 0)])
# print(listt)


# my_list = list(filter(lambda x: type(x)==int, [124, 1.2, 42, 65, 76]))
# print(my_list)


# name = ['a','b','c']
# money = [ 123,346,123]
# my_list = list(zip(name,money))
# print(my_list)


# name = ['a','b','c']
# my_list = tuple(enumerate(name))
# print(my_list)


# 1. В файле находится N натуральных чисел, записанных через пробел.
# Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найдите это число

my_list = [1, 5, 2, 3, 4, 6, 1, 7]
res = [my_list[0]]
for i in range(1, len(my_list)):
if my_list[i] - res[-1] > 0:
    res.append(my_list[i])

print(res)