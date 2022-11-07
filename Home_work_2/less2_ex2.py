from calendar import isleap

year = int(input('Введіть рік: '))

'''Варіант перший'''
# if isleap(year) == True:
#     print(f'{year} рік високосний!')
# else:
#     print(f'{year} рік не високосний!')

'''Варіант другий'''
# is_year_leap = isleap(year)
# string = f'Цей рік {is_year_leap}!'
# mod_string = string.replace('False', 'не високосний')
# mod_string = mod_string.replace('True', 'високосний')
# print(mod_string)

'''Варіант третій'''
# coef = [4, 100, 400]  # Кофіцієнт кратності
# is_year_leap = year % coef[0] == 0 and year % coef[1] != 0 or year % coef[2] == 0
# string = f'Цей рік {is_year_leap}!'
# mod_string = string.replace('False', 'не високосний')
# mod_string = mod_string.replace('True', 'високосний')
# print(mod_string)
