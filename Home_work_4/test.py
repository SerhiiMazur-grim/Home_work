my_list = [32, 43, 1, 3, 4, 5, 34, 5, 1, 7, 10, 34, 17, 11, 45, 1, 2, 3, 4, 5, 23, 22]

if len(my_list) <= 5:
    print(sorted(my_list))
else:
    j, k = 0, 5
    while j < len(my_list):
        my_list[j:k] = sorted(my_list[j:k], reverse = j % 2)
        j += 5
        k += 5
    print(my_list)