# Определить, является ли год, который ввел пользователем,
# високосным или не високосным.

years = int(input('Enter year'))
if years % 4 == 0:
    if years % 100 == 0:
        if years % 400 == 0:
            print('multiple of 100 and 400, hence a leap year')
        else:
            print('multiple of 100, but not multiple of 400, hence not a leap year')
    else:
        print('leap year')
else:
    print('not multiple of 4, hence not a leap year')