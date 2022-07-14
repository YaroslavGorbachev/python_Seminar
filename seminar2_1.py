# list() - список : изменяемый,индексируемый
# tuple()- кортеж: неизменяемый, индексируемый
# set()- множества: изменяемый, неиндексируемый
# dict()- словарь: изменяемый,индексируемый по ключу

#кортеж
# my_tuple = tuple([1,2,3])
# my_tuple = (1,2,3)
# # my_tuple = 10, кортеж в 1 элемент
# print(my_tuple)

#множества
# my_set = set()
# my_set = {4,2,7}
# print(my_set)

#словарь
# my_dict = dict()
# my_dict = {
#     123:"Стул",
#     753:"Стол"}

# # 1. Задайте список. Напишите программу, которая определит, присутствует
# # ли в заданном списке строк некое число.

# 1 решение

# list = ['123', '321', '456', '96']
# count = '2'
# array_find = []
# for find_count in list:
#     if count in find_count:
#         array_find.append(find_count)
# print(array_find)

# 2 решения

# str_list = ['12asd36', '256', 'dsds89358', '5698a']
# s_nym = input('Enter the number: ')
# is_Found = False
# for item in str_list:
#     print(item)
#     if item.__contains__(s_nym):
#         is_Found = True
#         break
# print(is_Found)


# #Напишите программу, которая определит позицию второго вхождения строки 
# #в списке либо сообщит, что её нет.

# list2 = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
# count2 = 'qwe'
# chec = 0
# for index in range(len(list2)):
#     if count2 == list2[index]:
#         chec += 1
#         if chec > 1:
#             print(f'второе вхождение: {index}')
#             break
# else:
#     print('нет таких')

# #Реализуйте алгоритм задания случайных чисел без использования встроенного
# #генератора псевдослучайных чисел.
# import time
# limit = int(input("Введите верхний предел: "))
# rnd_number = str(time.time())
# rnd_number = rnd_number.split(".")
# rnd_number = int(rnd_number[1])
# def random_number(number: int,limiy:int):
#     while True:
#         if number > limit:
#             number //= 10
#         else:
#            return number
# print(random_number(rnd_number,limit))