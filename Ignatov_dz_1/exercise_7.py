"""По длинам трех отрезков, введенных пользователем, определить возможность существования треугольника,
составленного из этих отрезков. Если такой треугольник существует, то определить, является ли
 он разносторонним, равнобедренным или равносторонним."""
a = input('enter the length of the first segment')
b = input('enter the length of the second segment')
c = input('enter the length of the third segment')
if a.isdigit() and b.isdigit() and c.isdigit():
    if int(a) + int(b) > int(c) and int(b) + int(c) > int(a) and int(a) + int(c) > int(b):
        print('triangle is possible')
        if int(a) == int(b) == int(c):
            print('triangle is equilateral')
        elif int(a) == int(b) or int(b) == int(c) or int(c) == int(a):
            print('isosceles triangle')
        else:
            print('triangle is versatile')
    else:
        print('triangle is not possible')
else:
    print('enter digits')
