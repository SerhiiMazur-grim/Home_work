'''2.Створити рядок розмір, якого не менше 5 символів і не більше 15,
    Обміняти місцями половини рядка при чому в другій половині рядка перетворити
	останні 3 літери у великі.'''

my_str = 'abcdefghij'
if 5 <= len(my_str) <= 15:
    mid_str = len(my_str) // 2
    my_str = my_str[mid_str:-3] + my_str[-3:].upper() + my_str[:mid_str]
    print(my_str)
else:
    print(f'У рядку {len(my_str)} символів, що не відповідає необхідному діапазону 5-15 символів!')

