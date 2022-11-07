# year = int(input('Введіть рік: '))
#
# coef = [4, 100, 400]  # Кофіцієнт кратності
# if year % coef[0] == 0 and year % coef[1] != 0 or year % coef[2] == 0:
#     print(f'{year} рік високосний!')
# else:
#     print(f'{year} рік не високосний!')

year = 2024

coef = [4, 100, 400]  # Кофіцієнт кратності
for i in coef:
    if year % coef[0] == 0 and year % coef[1] != 0 or year % coef[2] == 0:
        print(f'{year} рік високосний!')
    else:
        print(f'{year} рік не високосний!')

