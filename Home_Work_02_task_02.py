num = int(input('Введите целое число: '))
number = num
hexadecimal_digits = "0123456789ABCDEF"
hexadecimal_number = ""

while number > 0:
    remainder = number % 16
    hexadecimal_digit = hexadecimal_digits[remainder]
    hexadecimal_number = hexadecimal_digit + hexadecimal_number
    number //= 16

print(f'Шестнадцатеричное представление числа: {num}: 0x{hexadecimal_number}')
print(f'Проверка результата:', hex(num))
