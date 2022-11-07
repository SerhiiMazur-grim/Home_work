'''Створити алгоритм, який дозволить вивести на екран
	(порожній, тобто лише межі квадрата) квадрат із символів #
	Можна використовувати лише(всі інші можна окрім операторів виводу) наступні оператори print:
	print("#",end="")
	print(" ",end="")
	print("") #перехід на новий рядок, якщо треба.
	Вище буде оцінено рішення з введенням розміру квадрата з клавіатури)'''


''' Варіант №1 алгоритму для виводу фігури яка візуально максимально наближена до квадрата.
    Найкраще працює якщо довжина квадрата вказана не меньше 8-ми. '''

sqr_size = int(input('Введіть довжину квадрата (бажано не меньше 8-ми): '))

counter = 0

while True:
    if counter < sqr_size:
        print("#", end="")
        counter += 1
        if counter == sqr_size:
            print("")
        continue
    if counter == sqr_size:
        for i in range(int(sqr_size // 3)):
            print("#", end="")
            for i in range(sqr_size - 2):
                print(" ", end="")
            print("#", end="")
            print("")
        counter += 1
    if counter <= sqr_size * 2:
        print("#", end="")
        counter += 1
        continue
    break

''' Варіант №2 алгоритму для виводу квадрата де усі сторони рівні за кількістю символів "#". '''

# sqr_size = int(input('Введіть довжину квадрата : '))
#
# counter = 0
#
# while True:
#     if counter < sqr_size:
#         print("#", end="")
#         counter += 1
#         if counter == sqr_size:
#             print("")
#         continue
#     if counter == sqr_size:
#         for i in range(int(sqr_size - 2)):
#             print("#", end="")
#             for i in range(sqr_size - 2):
#                 print(" ", end="")
#             print("#", end="")
#             print("")
#         counter += 1
#     if counter <= sqr_size * 2:
#         print("#", end="")
#         counter += 1
#         continue
#     break
