# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке, из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.


import os
import shutil


print(f"Директория данного проекта {os.getcwd()}")


def make_dir(i):
    os.mkdir(f"{i}")


def remove_dir(i):
    os.rmdir(f"{i}")


def change_dir(i):
    os.chdir(i)


for r in range(9):
    make_dir(f"dir_{r+1}")

print(os.listdir())

for r in range(9):
    remove_dir(f"dir_{r+1}")


# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.


def current_dir():
    print(f"В данной папке находятся следующие файлы и папки: {os.listdir()}")


current_dir()

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.


def copy_current_file():
    current_file = os.path.realpath(__file__)
    copied_file = current_file + ".copy.py"
    if not os.path.isfile(copied_file):
        shutil.copy(current_file, copied_file)
        return copied_file + " - создан"
    else:
        return "Файл уже существует"


print(copy_current_file())
