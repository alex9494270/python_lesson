my_list = list(input("Введите число без пробелов = "))
for i in range(1, len(my_list), 2): #1 после range показывает с какого i начинаем?
    my_list[i-1], my_list[i] = my_list[i], my_list[i-1]

print(my_list)