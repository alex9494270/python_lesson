number = int(input('Введите натуральное число '))
maximum = number % 10
num = number

while num > 0:
    digit = num % 10
    if digit > maximum:
        maximum = digit

    if digit == 9:
        break

    num //= 10
    print (num)

print (f'Наибольшая цифра в числе {number} равна {maximum}')