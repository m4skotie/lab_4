a = int(input('Введите число: '))
if a%3 == 0 and a != 0:
    print('Число', a, 'делится на 3')
else:
    print('Число', a, 'не делится на 3')

def z2():
    try:
        a = int(input('Введите число: '))
        b = 100 / a
    except ZeroDivisionError:
        print('Введён 0')
    except ValueError:
        print('Введено не число ')
    else:
        print('100 / 2 = ', b)

def z3():
    a= input("Введите дату: ")
    if int(a[:2]) * int(a[3:5]) == int(a[-2:]):
        print("True")
    else:
        print("False")

def z4():
    a= input("Введите номер билета: ")
    if len(a) % 2 == 1:
        print("Чел ты...")
    else:
        b = int(len(a)/2)
        s = 0
        for i in range(b):
            s += int(a[i])
        s2 = 0
        for i in range(b):
            s2 += int(a[-(i+1)])
        else:
            if s == s2:
                print("Это счастливый билет")
            else:
                print("Это не счастливый билет")
z2()
z3()
z4()
