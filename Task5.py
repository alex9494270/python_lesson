revenue = input('Введите выручку за год')
costs = input('Введите затраты за год')

a = int(revenue)
b = int(costs)

if a > b:
    print(f'Прибыль составляет {a-b}')
    print(f"Рентабильность составляет {((a-b)/a)*100}%")
    human_capital = input('Введите количество сотрудников')
    c = int(human_capital)
    print(f'Прибыль на каждого сотрудника составляет {(a-b)/c}')
else:
    if a == b:
        print('Компания с нулевой прибылью')
    else:
        print('Компания убыточна')
print ('Конец программы')