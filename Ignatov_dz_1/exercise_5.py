# Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят,
# и сколько между ними находится букв.

letter_1 = input('enter one latin letter_1')
letter_2 = input('enter one latin letter_2')
if letter_1.isalpha() and letter_2.isalpha() and len(letter_1) == 1 and len(letter_2) == 1:
    x = ord(letter_1) - 96
    y = ord(letter_2) - 96
    print(f'the first letter position is: {x}')
    print(f'the second letter position is: {y}')
    if x > y:
        print(f'the number of characters between letters is: {x - y - 1}')
    else:
        print(f'the number of characters between letters is: {y - x - 1}')
else:
    print('enter one latin letter!')