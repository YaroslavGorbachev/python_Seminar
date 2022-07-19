# path = 'file.txt'
# with open(path,'r') as f:
#     data = f.readline()
#     print(data)

# # Считать строку из файла. Напишите программу, которая покажет большее и меньшее число. 
# # В качестве символа-разделителя используйте пробел.

# from importlib.resources import path

# path =r'file.txt'
# with open(path, 'r')as f:
#     list = f.readline().split(' ')

#     print(max(list))
#     print(min(list))

# def is_int(str: str) -> bool:
#     try:
#         int(str)
#         return True
#     except ValueError:
#         return False


# def input_list_int_numbers(str_in: str) -> list:
#     list_dirty = str_in.split(' ')
#     list_clean = []
#     for elem in list_dirty:
#         if is_int(elem):
#             list_clean.append(int(elem))
#     return list_clean
# import os

# def convert_to_int(str):
#     return [int(x) for x in str.split()]

# path = os.path.join('folder', 'file.txt')


# with open(path, 'r'):
#     text = writer.readline()

# int_list = convert_to_int(text)


# print(int_list)
# print(max(int_list))
# print(min(int_list))


# f = open('str_file', 'r')
# str_in = f.readline()
# f.close()

# numb_list = input_list_int_numbers(str_in)

# print(numb_list)
# print(max(numb_list))
# print(min(numb_list))

# import os

# def convert_to_int(str):
#     return [int(x) for x in str.split()]

# path = os.path.join('folder', 'file.txt')


# with open(path, 'r') as writer:
#     text = writer.readline()

# int_list = convert_to_int(text)


# print(int_list)
# print(max(int_list))
# print(min(int_list))

# # 2. Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:
# 1) с помощью математических формул нахождения корней квадратного уравнения
# 2) с помощью дополнительных библиотек Python


# path = r'Testfiles/S4T2.txt'

# with open(path, 'r') as f:
#     a = int(f.readline())
#     b = int(f.readline())
#     c = int(f.readline())

# disc = b**2 - 4 * a * c
# x1 = -b + (disc**(1/2) / (2 * a))
# x2 = -b - (disc**(1/2) / (2 * a))
# print(x1, x2)

# with open(path, 'a') as f:
#     f.write(f'\nКорень 1: {x1}')
#     f.write(f'\nКорень 2: {x2}')

# import os

# def is_int(str: str) -> bool:# проверка на инт
#     try:
#         int(str)
#         return True
#     except ValueError:
#         return False
# def input_list_int_numbers(str_in: str) -> list:# создает список  цифр
#     list_dirty = str_in
#     list_clean = []
#     for elem in list_dirty:
#         if is_int(elem):
#             list_clean.append(int(elem))
#     return list_clean
# path = r'folder\disk.txt'

# with open(path, 'r') as d:
#     list = d.read().split("\n")
#     print(list)

# list2 = input_list_int_numbers(list)
# print(list2)

# d = list2[1]**2 - 4* list2[0] * list2[2]
# print(d)

# with open(path, 'a') as f:
#     f.write(f'')
