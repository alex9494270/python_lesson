string = input("Введите слова через пробелы - ").split()
for i, word in enumerate(string, 1): #получается, что тут мы сразу создали новую переменную word?
    print(f'{i}, {word[:10]}')