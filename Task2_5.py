my_list = [10, 8, 7, 5, 5, 3, 3, 3, 1]
new_number = int(input('Введите любое натурально число - '))
i = 0

for n in my_list:
    if new_number <= n:
        i += 1

    elif new_number >n:
        break

my_list.insert(i, new_number)
print(my_list)