from random import randint
num = randint(0, 1000)
attempts = 10

print("Угадаете число от 0 до 1000 за 10 попыток?")

number = int(input("Отлично! Введите число: "))
if number < 0 or number > 1000:
    print("Введено неверное число. Введите число от 0 до 1000.")

else:
    while attempts > 0:
        if number > num:
            print(f"Загаданное число меньше {number}")
            attempts -= 1
            if attempts == 0:
                number = int(input(f'Это последняя попытка. Введите число:  '))
            else:
                number = int(input(f'Осталось {attempts} попыток. Введите число:  '))

        elif number < num:
            print(f"Загаданное число больше {number}")
            attempts -= 1
            if attempts == 0:
                number = int(input(f'Это последняя попытка. Введите число:  '))
            else:
                number = int(input(f'Осталось {attempts} попыток. Введите число:  '))

        else:
            print(f'Ура!!! число угадано верно!!! Загаданное число, действительно, {num}')
            break


    print(f'Игра окончена! Было загадано число {num} ')





