"""sorted()  .sort()"""

# list_1 = [4,34, 243,6,132,2,5,0]

# list_1.sort()
# print(list_1)

# sorted(list_1)
# print(list_1)


# list_2 = [list_1.append(el) for el in range(4)]
# print(list_1)
# print(list_2)

"""#FUNCTION"""
# def - оператор який створює за вказаною назвою підпрограмму
#name_fun - ім'я функції
#ініціалізація функції
# def fun_1():
#     #тіло функції
#     print('Refaund')
#
# #main code
# print('main code')
# #виклик функції
# fun_1()
# fol = 100

"""Функція щось приймає і нічого не повертає"""
# def fun_1(par_1, par_2):
#     # global fol
#     print('fun_1')
#     par_1 += par_2
#
#     print(f"par_1 = {par_1}, par_2 = {par_2}")


#main code

# fun_1(43, 300)
# num_1 = int(input('Inp num_1: '))
# num_2 = int(input('Inp num_2: '))
#
# fun_1(num_1, num_2)

# list_1 = [23,4,4342,423]
# list_2 = [1,2,3,4,5]

# fun_1(list_1.copy(), list_2)
# fun_1(list_1[:], list_2)
# print(f'list_1 after fun_1: {list_1}')
"""Функція щось приймає і щось повертає"""
# def last_three(string):
#     if len(string) > 2:
#         # last_t = string[-3:]
#         # return last_t
#         return print( string[-3:])
#     else:
#         return string

# print(last_three('OdwIII'))
# str_1 = last_three('fhurf324')
# print(str_1)

# if last_three('jdowe324').isdigit():
#     print('is digit')

# last_three('fwjfiwePPP')


# def last_three(string, fun):
#     if fun(string) > 2:
#         # last_t = string[-3:]
#         # return last_t
#         return print( string[-3:])
#     else:
#         return string
#
#
# last_three('fwehfueiW', len)

"""Функція нічого не приймає і щось повертає"""
# str_1 = 'fjoiwjfiweffwe'
# print(str_1.upper())

# def fun_1():
#     return f'sum = {24 + 234}'

"""Функція нічого не приймає і нічого не повертає"""
# list_1 = [243,4, 2,52,234, 4,3423,423]
# print(list_1.sort())


# def fun_1(par_1, - обов'язковий параметр з динамічною типізацією
#           par_2 = "default value", - не обов'язковий параметр)

# def fun_1(par_1, par_2 = "default value"):
#     print(par_1)
#     print(par_2)


# fun_1(34)
# fun_1(322, 2342)

# fun_1(par_2='iwehfioew', par_1=42342)
"""Рекомендована типізація"""
# def fun_3(alias:str, roll:int, lister:list):
#     print('inside fun')


# fun_3(23423, 'wifjiwof', 2423.4234)


# def fun_3(alias:str = 'Empty', roll:int = 4, lister:list = []):
#     print('inside fun')
#
#
# fun_3()
# fun_3('LOl')
# fun_3('wifw', 454)
# fun_3('POe', 32234, [3,54,5,6])
# fun_3(lister=[4234,234,123,312], alias = 'ewdwe', roll=345)


# def fun_3(alias:str = 'Empty', roll:int = 4, lister:list = [])->list:
#     print('inside fun')
#     return lister


"""Summary"""
# def fun_3(alias:str = 'Empty', roll:int = 4, lister:list = [])->list:
#     """Короткий опис призначення функції, призначення параметрів, та що вона повертає"""
#
#     print('inside fun')
#     return lister
#
# fun_3()
"""* - oператор упаковки / розпаковки даних в кортеж"""
# def sum_el(*lol):
#     print(lol)
#
# sum_el(24, 42,34 ,234 ,234,234,231,11,1,32)

# list_1 = [123, 23,4,12,3123,312]
# print(*list_1)

"""Порядок створення пареметрів функцій"""
# def fun_5( to, #Обов'язковий параметр
#            re:int, #Обов'язковий параметр з рекомендуємим типом
#            frk:int = 234, # НЕ Обов'язковий параметр з рекомендуємим типом та default значенням
#            trf = True,  # НЕ Обов'язковий параметр з default значенням
#            *args, #Параметр з пакувальником в кортеж
#            **kwargs, #Параметр з пакувальником в словник
#            ):
#     pass

"""Латентний return"""
# def fun_6():
#     print('fwjefoiewj')
#
# print(fun_6())
"""lambda - однорядкові / анонімні функції"""

def powered(num_1:int, num_2:int)->int:
    if num_1 > num_2:
        return num_1 ** num_2
    elif num_1 == num_2:
        return num_1 + num_2
    else:
        return num_2 ** num_1

    # return  num_1 ** num_2 if num_1 > num_2 else num_2 ** num_1
    # return num_1 > num_2 and num_1 ** num_2 or num_2 ** num_1

# print(powered(23, 2))
# print(lambda num_1, num_2: num_1 ** num_2)

# l = lambda num_1, num_2: num_1 ** num_2
# print(l(3,4))

#IIFE - виконання функцій в місці створення

# print( (lambda num_1, num_2: num_1 ** num_2)(23,2)  )

""""""
#Відсортувати список рядків
# list_1 = ['1a', 'lol', 'a', 'f', 'F', '   ', '\ne']
# print(sorted(list_1))
# print(sorted(list_1, key=len))
# def second_elem(st:str)->str:
#     return st[1] if len(st) > 1 else st


# print(sorted(list_1, key = lambda st: st[1] if len(st) > 1 else st))


# print(lambda st: st[1] if len(st) > 1 else (lambda om: om * 4)(st))


"""list compre"""
# print(lambda y, x: [el for el in range(y,x)])

#Packing tuple
# print( (lambda *args: [el for el in args]) (4234, 24,2,413,213,12,3142,5))
