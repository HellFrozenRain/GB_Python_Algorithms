# Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

number = input('Enter a three-digit number')
if number.isdigit() == True:
    if len(number) != 3:
        print('enter a THREE-digit number!')
    else:
        print(f'number: {number}')
        x = int(int(number[0]))
        y = int(int(number[1]))
        z = int(int(number[2]))
        total = x + y + z
        print(f'the sum is: {total}')
        multiplication = x * y * z
        print(f'multiplication is: {multiplication}')
else:
    print('enter a three-digit NUMBER!')