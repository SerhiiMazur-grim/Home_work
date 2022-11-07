'''3.Створити рядок розміром не більше 10 символів та останні три
	символи перетворити на маленькі літери та перемістити в середину
	остачі символів(окрім 3ох останніх) рядка.'''

my_str = 'ABCDEFGHI'
if my_str and len(my_str)<=10:
    mid_str = len(my_str[:-3])//2
    my_str = my_str[:mid_str] + my_str[-3:].lower() + my_str[mid_str:-3]
    print(my_str)
elif len(my_str) == 0:
    print(f'У рядку {len(my_str)} символів!')
else:
    print(f'У рядку {len(my_str)} символів, довжина рядка не повинна перевищувати 10 символів!')