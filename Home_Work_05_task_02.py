"""Напишите функцию, которая принимает на вход строку -
абсолютный путь до файла. Функция возвращает кортеж из трёх
элементов: путь, имя файла, расширение файла."""
def get_file_info(file_path):
    #находим индекс последнего вхождения символа слэш
    last_slash = file_path.rfind('/')
    #получаем путь до файла
    get_path = file_path[:last_slash + 1]

    #Находим индекс последнего вхождения символа .
    last_dot = file_path.rfind('.')
    #если символ не найден возвращаем пустую строку
    if last_dot == -1:
        get_path = file_path[last_slash]
        extension = ''
    else:
        file_name = file_path[last_slash + 1:last_dot]
        extension = file_path[last_dot: ]
        #возвращаем кортеж из 3х элементов

    return get_path, file_name, extension

file_path = "C:/Users/User/Documents/example.txt"
info = get_file_info(file_path)
print(info)
