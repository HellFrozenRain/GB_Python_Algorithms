# Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

letter_num = input('enter number between 1 and 26')
if letter_num.isdigit() and 1 <= int(letter_num) <= 26:
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    print(alphabet[int(letter_num) - 1])
else:
    print('try again')