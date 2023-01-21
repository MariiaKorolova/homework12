#1. Инициализация класса с одним параметром - имя директории.

import os
# Создать класс
class Person:
    # Создание параметра текущей директории
    def __init__(self, dir_name: str):
        self.dirname = dir_name

# 2. Написать метод класса, который создает атрибут класса в ввиде словаря
# {'filenames': [список файлов в папке], 'dirnames': [список всех подпапок в папке]}.
# Подпапки учитывать только первого уровня вложения. Папка в папке в папке - такое не брать ))
# {'filenames': [файл1, файл2, файл7], 'dirnames': [папка1, папка2]}

# Cоздание метода класса, который создает атрибут класса в ввиде словаря
    @staticmethod
    def dict_creator(dir_name=None):
        data = os.listdir(dir_name)
        # Создание словаря с 2 ключами
        dictionary = dict.fromkeys(['filenames', 'dirnames'])
        # 2 пустых списка
        dirnames = []
        filenames = []
        for i in data:
            if ".fleet" in i or ".git" in i or ".idea" in i or "__pycache__" in i:
                pass
            elif "." not in i:
                dirnames.append(i)
            else:
                filenames.append(i)
        dictionary['dirnames'] = dirnames
        dictionary['filenames'] = filenames
        return dictionary

# 2. Написать метод класса, которая получает булевое значение (True/False).
# Функция возвращает тот же словарь, но с отсортированными именами файлов и папок в соответствующих списках.
# Булевое значение True означает, что порядок сортировки алфавитный, False - обратный порядок.

# Сортировка
    @staticmethod
    def dictionary_sorter(reverse=None):
        # Если reverse +, то сортируем список по алфавиту
        if reverse:
            sorter_filenames = data_dictionary['filenames']
            sorter_filenames.sort()
            sorter_dirnames = data_dictionary['dirnames']
            sorter_dirnames.sort()
        # Если reverse -, то сортируем список по в обратном порядке
        else:
            sorter_filenames = data_dictionary['filenames']
            sorter_filenames.sort(reverse=True)
            sorter_dirnames = data_dictionary['dirnames']
            sorter_dirnames.sort(reverse=True)
        return data_dictionary

# 3. Написать метод класса, которая получает строку, которая может быть
# или именем файла, или именем папки. (В имени файла должна быть точка).
# В зависимости от того, что функция получила (имя файла или имя папки) - записать его
# в соответствующий список и вернуть обновленный словарь.

 # Создаем новый метод
    @staticmethod
    def new_file_method(name):
        # Если это файл, добавить в список файлов в словаре
        if "." in name:
            new_file = data_dictionary['filenames']
            new_file.append(name)
            data_dictionary['filenames'] = new_file
        # Если нет, добавить в список папок в словаре
        else:
            new_dir = data_dictionary['dirnames']
            new_dir.append(name)
            data_dictionary['dirnames'] = new_dir
        return data_dictionary

# 4* (*сдавать не обязательно, но если будете сдавать, то ошибки будут учитываться тоже).
# Написать метод класса, которая получает имя директори и словарь по примеру из задания 1.
# Функция проверяет соответствие полученного словаря и реальной файловой системы в полученной папке и,
# если надо, создает нужные папки и пустые файлы, в соответствии со структурой словаря.
# Пример-создали на основании данных в папке -> {'filenames': [файл1, файл2, файл7], 'dirnames': [папка1, папка2]}
# передали в метод -> {'filenames': [файл1, файл7, файл13], 'dirnames': [папка11, папка2]}
# в результате необходимо создать файл13 и папка11

