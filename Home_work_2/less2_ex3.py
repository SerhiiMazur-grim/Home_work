# num1 = int(input('Введіть перше ціле число: '))
# num2 = int(input('Введіть друге ціле число: '))
# num3 = int(input('Введіть третє ціле число: '))

num1 = 2
num2 = 5
num3 = 18
#
# num_list = []
#
# for num in range(1, num3+1):
#     if num % num1 == 0 and num % num2 == 0:
#         num_list.append('FB')
#     elif num % num1 == 0:
#         num_list.append('F')
#     elif num % num2 == 0:
#         num_list.append('B')
#     else:
#         num_list.append(str(num))
#
# num_str = ' '.join(num_list)
# print(num_str)

num1 = 2
num2 = 5
num3 = 18

num1 = int(input('Введіть перше ціле число: '))
num2 = int(input('Введіть друге ціле число: '))
num3 = int(input('Введіть третє ціле число: '))


num_list = []

for num in range(1, num3+1):
    if num % num1 == 0 and num % num2 == 0:
        num = 'FB'
    elif num % num1 == 0:
        num = 'F'
    elif num % num2 == 0:
        num = 'B'
    num_list.append(str(num))
num_str = ' '.join(num_list)
print(num_str)
