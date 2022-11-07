'''1.  Частина рядка(Easy: 0.3 point)
	Отримати з клавіатури рядок, у якому буква h зустрічається щонайменше двічі.
	Виведіть послідовність символів, укладену між першою та останньою появою літери h, у
	протилежному порядку.
	'''

'''Var_1'''
# my_str = 'somehworldheLlo'
# # my_str = str(input('Введіть рядок:'))
# my_str = my_str[my_str.find('h')+1:my_str.rfind('h')][::-1]
# print(my_str)

'''Var_2'''
# my_str = my_str.split('h')[1][::-1]
# print(my_str)


'''2. Рядки та списки(Easy: 0.5 point)
	Отримати з клавіатури рядок, та записати в список кількість великих, маленьких, цифр, та інших знаків.
	'//LLOOab cde67890' ➞ [4, 5, 5, 3] '''

# my_str = '//LLOOab cde67890'
# # my_str = str(input('Введіть рядок:'))
# my_list = [0, 0, 0, 0]
# for i in my_str:
#     if i.isalpha():
#         if i.isupper():
#             my_list[0] +=1
#         else:
#             my_list[1] += 1
#     elif i.isdigit():
#         my_list[2] += 1
#     else:
#         my_list[3] += 1
#
# print(my_list)

'''3. Рядки та списки (Easy: 0.5 point )
	Отримати з клавіатури рядок. Знайти всі цифри рядка та записати їх як елементи списку.
	Наприклад:
	'wfuhw312mjs19sj1d04' ➞ [3, 1, 2, 1, 9, 0, 4]'''

# # my_str = 'wfuhw312mjs19sj1d04'
# my_str = str(input('Введіть рядок:'))
# my_str = [int(i) for i in my_str if i.isdigit()]
# print(my_str)

'''4. Функції та рядки (Easy: 0.5 point)
	Свторити функцію, яка приймає рядок, видаляє всі пробіли окрім останнього та повертає рядок у відповіді.
	'Simple, remove the spaces from the string' ➞ "Simple,removethespacesfromthe string" '''

# def my_funk(string:str):
#     my_list = string.split(' ')
#     return ''.join(my_list[:-1]) + ' ' + my_list[-1]
#
# print(my_funk('Simple, remove the spaces from the string'))

'''5.  Функції та списки (Easy: 0.5 point)
	Свторити функцію, яка приймає список, перетворює всі елементи списка на рядок, та 
	повертає результат у вигляді рядка, 
	який складається з елементів списку розділених пробілом.(*використати як умога коротший спосіб)
	[32, 4.43, 'lister', False, None, [1,2,3,4]] ➞ "32 4.43 lister False None [1,2,3,4]" '''

# def my_func(some_list:list):
#     return ' '.join(str(i) for i in some_list).strip()
#
# print(my_func([32, 4.43, 'lister', False, None, [1,2,3,4]]))

''' 6. Словники. (Middle: 1 point)
	Створити алгоритм гри "Містечка". Тобто правила такі:
	Є словник із столицями країн. (10 столиць країн на твій вибір)
	Користувач "нескінченно" вводить назву міст і програма на основі словника видає відповідь так 
	це столиця такої країни чи ні на жаль це не столиця якщо такої столиці у 10 країн зі словника немає. 
	або введіть слово стоп, яке закінчить цикл.
 '''


# data = {
#         'Ukraine' : 'Kyiv',
#         'Armenia' : 'Yerevan',
#         'Australia' : 'Canberra',
#         'Austria' : 'Vienna',
#         'Belgium' : 'Brussels',
#         'Bulgaria' : 'Sofia',
#         'Denmark' : 'Copenhagen',
#         'Finland' : 'Helsinki',
#         'France' : 'Paris',
#         'GermanyGermany': 'Berlin'
#     }
#
#
# while True:
#     inp_str = input('Enter the name of the capital: ')
#     if inp_str != 'stop':
#         if inp_str in data.values():
#             for k, v in data.items():
#                 if v == inp_str:
#                     print(f'Так, це столиця {k}.')
#                     continue
#         else:
#             print('Hі на жаль це не столиця.')
#             continue
#     else:
#         break

''' 7. Перетворення словників (Middle: 1 point)
	Створити на основі англо-латинського словника латино-англійський словник.
	Тобто на основі прикладу нижче створити алгоритм, який перетворить словник мовою python)
	Вхідні дані (словник приклад):
		{ "apple" : ['malum', 'omum', 'popula'],
		'fruit' : ['baca', 'bacca', 'popum'],
		'punishment' : ['malum', 'multa'],
		'dog' : 'canina'}
	На виході отримаємо:
	{'malum': ['apple', 'punishment'], 
	'omum': 'apple', 
	'popula': 'apple', 
	'baca': 'fruit', 
	'bacca': 'fruit', 
	'popum': 'fruit', 
	'multa': 'punishment', 
	'canina': 'dog'}
	
	*Відповідь робити не руками а алгоритмом! Тобто вхідний словник перетворити алгоритмом на словник 
	латино-англійських слів
	**словник приклад - це означає, що даний словник є зразковим, а ваш алгоритм буде протестований на 
	більшому словнику, 
	  тобто немає сенсу писати підігнаний алгоритм, а необхідно написати універсальний алгоритм. '''

# def my_dict(some_dict):
#     new_dict = {}
#     for k, v in some_dict.items():
#         if type(v) is list or set:
#             for el in v:
#                 new_dict[el] = k
#         else:
#             new_dict[v] = k
#     return new_dict
#
# print(my_dict({ "apple" : ['malum', 'omum', 'popula'],
# 		'fruit' : ['baca', 'bacca', 'popum'],
# 		'punishment' : ['malum', 'multa'],
# 		'dog' : 'canina'}))


''' 8. Рядкові паттерни (Middle*: 1.5 point)
	Створіть функцію, яка перевіряє, чи даний рядок складається з шаблону підрядка,
	який повторюється кілька разів на протязі вього рядка, то повернути True або False якщо такого шаблону не існує.

	приклади:
	"a" ➞ False
	"ababab" ➞ True
	"aabb" ➞ False
	"abcabcabcabc" ➞ True
	"abcabccba" ➞ False
	"aaaa" ➞ True '''


# def my_funk(string:str):
#     ''' Примітка: опираючись на перший та останній приклади я зрозумів що непарна кількість
#               однакових символів дає False '''
#     patt = string[:string.find(string[0], 2)]
#     new_str = string.replace(patt, '')
#     return True if not new_str else False
# #
# print(my_funk('a'))
# print(my_funk('ababab'))
# print(my_funk('aabb'))
# print(my_funk('abcabcabcabc'))
# print(my_funk('abcabccba'))
# print(my_funk('aaaa'))
# print(my_funk('asdfgasdfg'))


''' 9. Дужки та рядки (Middle**: 1.7 point)
	Cтворити функцію, яка приймає рядок дужок і повертає допустимий порядок фігурних дужок чи ні.
	Всі вхідні рядки будуть непустими і будуть складатися тільки з дужок: () [] {}. 
	Що вважається дійсним? Рядок фігурних дужок вважається дійсним, якщо всі дужки складаються в правильну послідовність, 
	тобто є відкриті та закриті дужки одного виду на оденому рівні.
	Приклади:
	"(){}[]" ➞ True 
	"([{}])"  ➞ True  
	"(}"    ➞ False  
	"[(])"  ➞ False 
	"[({})](]" ➞ False '''


# def my_funk(string):
#     brackets = [['(', '[', '{'], [')', ']', '}']]
#     temp = []
#     if string and len(string) % 2 == 0 and string[0] in brackets[0]:
#         for i in string:
#             if i in brackets[0]:
#                 temp.append(i)
#             elif i in brackets[1]:
#                 open_brec = brackets[0][brackets[1].index(i)]
#                 if temp[-1] == open_brec:
#                     temp.pop()
#                 else:
#                     return False
#         return True
#     return False
#
#
# print(my_funk("(){}[]"))
# print(my_funk("([{}])"))
# print(my_funk("(}]"))
# print(my_funk("[(]"))
# print(my_funk("[({})](]"))


''' 10. Файли та рядки (Hard: 2.5 point)
	Обробити файл (файл у додатку до завдання) та знайти найдовше слово в даному файлі(file_1.txt). 
	Далі Дoзаписати це слово назад у файл, але тільки всі літери повинні бути КАПСОМ (записати теж слово, 
	але тільки великими літерами). '''

# with open('file_1.txt', 'r+', encoding='utf=8') as file:
#     rows = file.read()
#     sort_list = sorted(rows.split(), key=len, reverse=True)
#     file.write('\n\n' + sort_list[0].upper())

