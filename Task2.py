a = input('Введите количество секунд ')
if int(a) >= 0:
    hours = int(a)//3600
    minutes = int(a)%3600//60
    seconds = int(a)%3600%60

    if hours < 10 and minutes < 10 and seconds < 10:
        print(f'0{hours}:0{minutes}:0{seconds}')
    else:
        if hours < 10 and minutes < 10 and seconds >= 10:
            print(f'0{hours}:0{minutes}:{seconds}')
        else:
            if hours < 10 and minutes >= 10 and seconds >= 10:
                print(f'0{hours}:{minutes}:{seconds}')
            else:
                if hours >= 10 and minutes >= 10 and seconds >= 10:
                    print(f'{hours}:{minutes}:{seconds}')
                else:
                    if hours >= 10 and minutes >= 10 and seconds < 10:
                        print(f'{hours}:{minutes}:0{seconds}')
                    else:
                        if hours >= 10 and minutes < 10 and seconds < 10:
                            print(f'{hours}:0{minutes}:0{seconds}')
                        else:
                            if hours < 10 and minutes >= 10 and seconds < 10:
                                print(f'0{hours}:{minutes}:0{seconds}')
                            else:
                                if hours >= 10 and minutes < 10 and seconds >= 10:
                                    print(f'{hours}:0{minutes}:{seconds}')
else:
    print ('Секунды не могут быть отрицательными ')
print('Конец программы')