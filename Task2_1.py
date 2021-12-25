my_list = [5, 16.5, "name", [1, 2], (3, 0), {4: 5}]

for i, item in enumerate(my_list, 1):
    print((f"{item} - {type(item)}"))