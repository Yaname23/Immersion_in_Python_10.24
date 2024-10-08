# Задача на проверку простое ли число
def simple():
    num = int(input("Введите число: "))

    if num < 0 or num > 1000:
        return "Введено неверное число. Введите число от 0 до 1000."

    if num == 1 or num == 0:
        return "Число не относится ни к простым, ни к составным."

    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return f'Число {num} составное.'
    return f'Число {num} является простым.'

print(simple())