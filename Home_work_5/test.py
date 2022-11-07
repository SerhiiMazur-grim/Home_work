def sum_even_numbers(seq):
    return sum(i for i in seq if i % 2 == 0)

print(sum_even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))



# def filter_list(l):
#     return [i for i in l if type(i) == int]
#
# print(filter_list([1, 2, 'a', 'b']))

# def unique_sum(lst):
#     return sum(set(lst)) if lst else None
#
# print(unique_sum([1,3,8,1,8])) #12

# import datetime
# t = '01:20'
# m,s = t.split(':')
# print(int(datetime.timedelta(minutes=int(m),seconds=int(s)).total_seconds()))
#
# def longest_possible(playback):
#     t = playback
#     m, s = t.split(':')
#     print(int(datetime.timedelta(minutes=int(m), seconds=int(s)).total_seconds()))

# def byte_to_set(byte):
#   return {i for i in range(8) if "{0:08b}".format(byte)[i] == "1"}
# print(byte_to_set(255))

# print("{0:08b}".format(255))


# def car_crash(road):
#     road = ''.join(i for i in road.split('\n') if "O='`o" in i)
#     return False if road.find('X', road.index('o')) == -1 else True
#
# def car_crash(road):
#     return "O='`oX" in road.replace(' ', '')
#
# all_directions = """
#                          X   X  X
#                 X         O='`o   X
#                          X   X   X  """.strip()
#
# print(car_crash(all_directions))


# def is_it_a_num(s: str) -> str:
#     s = ''.join(i for i in s if i.isdigit())
#     if len(s) == 11 and s[0] == '0':
#         return s
#     return "Not a phone number"
#
# print(is_it_a_num("S:)0207ERGQREG88349F82!efRF)"))
# print(is_it_a_num("S:)207ERGQREG88349F82!efRF)"))

# def to_float_array(arr):
#     arr = [float(i) if '.' in i else int(i) for i in arr]
#     return arr
#
# print(to_float_array(["1.1", "2.2", "3.3"]))


# def has_unique_chars(string):
#     coun = 1
#     for i in string:
#         if string.count(i) != 1:
#             coun = string.count(i)
#     if coun == 1:
#         return True
#     return False
#
#
# print(has_unique_chars("abcdef"))
# print(has_unique_chars("++-"))

# def remove_smallest(numbers):
#     if numbers:
#         x = numbers.copy()
#         x.remove(min(x))
#         return x
#     return numbers
# print(remove_smallest([]))

# def take_second(elem):
#     return elem[1]
#
# def sort_dict(d):
#     d = sorted([(j, k) for j, k in d.items()], key=take_second, reverse=True)
#     return d

# def sort_dict(d):
#   return sorted(d.items(), key=lambda x: x[1], reverse=True)
#
# print(sort_dict({1:2, 2:4, 3:6}))

# import functools
#
# data1 = [[2, 5], [3, 4], [8, 7]]
# def process_data(data):
#     data = functools.reduce(lambda a, b : a * b, [i[0]-i[1] for i in data])
#     return data
# print(process_data(data1))

# def disemvowel(string_:str):
#     string_ = ''.join([i for i in string_ if i not in 'aeiouAEIOU'])
#     return string_
#
# print(disemvowel('some'))

# def get_count(sentence):
#     coun = 0
#     for i in sentence:
#         if i.lower() in 'aeiou':
#             coun += 1
#     return coun
#
# print(get_count('some'))