# def func(param_1=0, param_2=0,param_3=0 ,param_4=0)-> int:
#     summ = param_1 + param_2 + param_3 + param_4
#     return summ
# print(func(1,2,3,)) #print(func(1,param_4=1,param_3=2))

# def func(param_1, *args, **keys) -> int:
#     print(param_1, args, keys)
# func(1, 645, 856, 234, 745, 756, 123, 3423, key_1=123, key_2=55)

# #1. Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
# number = int(input("Введите количествыо шагов: "))
# def list_from(number: int):
#     list_numbers = []
#     for element in range (0, number):
#         list_numbers.append((-3)**element)
#     return list_numbers
# print(list_from(number))

# def sequence(n: int):
#     sequence_list = [1]
#     i = 0
#     while i < n-1:
#         sequence_list.append(sequence_list[i]*-3)
#         i += 1
#         return sequence_list
# n = int(input('Введите n: '))
# print(sequence(n))

# def Input_values(write_what_you_want: str):
#     for_checking = False
#     while not for_checking:
#         try:
#             number = int(input(f'{write_what_you_want}'))
#     for_checking = True
#         except ValueError:   
# print("Попробуй снова. Ты должен ввести число.")
# return number
# def progression(N:int):
#     help_number = 1
#     for i in range(N):
#     print(help_number)
# help_number = help_number * -3
# number_N = Input_values("Введите число N: ")
# progression(number_N)


# Напишите программу, в которой пользователь будет задавать
# две строки, а программа - определять количество вхождений одной строки в другой.

# org_text = input("Введите строку: ")
# find_text = input("Введите искомую строку: ")

# def text_finder(org_text: str, find_text: str):
#     counter = 0
#     for index in range (0, len(org_text) - len(find_text)+1):
#         if find_text in org_text[index:index+len(find_text)]: counter += 1
#     return counter
# print(f"Текст '{find_text}' втречается в тексте {text_finder(org_text, find_text)} раз")

# str_1 = 'Hello, world!ll'
# str_2 = 'll'
# count = 0
# for i in range(len(str_1) - len(str_2) + 1):
#     if str_1[i : i + len(str_2)] == str_2:
#         count += 1
# print(count)

# str_1 = 'Hello, world!ll'
# str_2 = 'll'
# count = 0
# for i in range(len(str_1) - len(str_2) + 1):
# if str_1[i : i + len(str_2)] == str_2:
# count += 1
# print(count)


# str_1 = 'Hello, world!ll'
# str_2 = 'll'
# print(str_1.count(str_2))

