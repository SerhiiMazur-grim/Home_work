'''2. Написати програму, яка вирішує математичний приклад з файлу(file_1.txt),
	а також записує результат назад до файлу.
	Приклад:
		Рядок у файлі
		34 + 22 - 11*10
		Після роботи вашої програми
		34 + 22 - 11 * 10 = -54
		ТОбто у файл записується відповідь після обчислення!
		(тобто приклад символ дорівнює і відповідь, потрібно записати
		у кожному рядку файла)
		Файл із завданням у додатку до дз.


	*Раджу загуглити метод для цих цілей)
	**Також раджу помаксимуму застосувати переваги функціонального пронграмування.'''



def calc_str(string:str):
    '''Функція приймає математичний вираз у вигляті рядка та обчислює його.
       Повертає функція результат обчислення рядка, або попередження, якщо
       присутня дія ділення на нуль.'''

    try:
        calc = round(eval(string),2)
        return str(calc)
    except ZeroDivisionError as err:
        print(f' {err} --->> На нуль не ділимо!')
        return 'На нуль не ділимо!'


def format_str_row(row:str):
    '''Функція приймає рядок і форматує його для кращого відображення.
       Повертає функція відформатований рядок.'''

    row = row.replace(' ', '')
    temp_list = [f' {el} ' if el in '+-*/%' else el for el in row]
    return ''.join(temp_list)



def file_work(file_name:str):
    '''Функція читає текстовий файл, форматує рядки за допомогою функції format_str_row(),
       обчислює математичний вираз за допомогою функції calc_str() і перезаписує у
       файл відформатований рядок з результатом обчислення'''

    with open(file_name, mode='r') as file:
        row_list = file.read().split('\n')

        formated_list = list(map(format_str_row, row_list))
        rez_list = list(map(calc_str, formated_list))
        rezult = list(' = '.join(i) for i in zip(formated_list, rez_list))

    with open(file_name, 'w') as file:
        for rez_row in rezult:
            file.write(rez_row + '\n')


file_work('file_1.txt')

