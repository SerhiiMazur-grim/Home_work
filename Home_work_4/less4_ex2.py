'''2. Написати алгоритм рішення fizzbuzz для 10 трійок чисел, які записані в файл (file_1.txt).
	Читайте із файлу перший рядок, берете із неї числа, рахуйте для них fizzbuzz, виводите. '''

with open('file_1.txt', 'r') as file:
    row_list = [row.split(' ') for row in file.read().split('\n')]

for row in row_list:
    fizz = int(row[0])
    buzz = int(row[1])
    end_range = int(row[2])

    num_list = []

    for num in range(1, end_range + 1):
        if num % fizz == 0 and num % buzz == 0:
            num = 'FB'
        elif num % fizz == 0:
            num = 'F'
        elif num % buzz == 0:
            num = 'B'
        num_list.append(str(num))
    num_str = ' '.join(num_list)
    print(num_str)
