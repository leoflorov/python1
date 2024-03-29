# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()

newList = ["яблоко", "банан", "киви", "арбуз"]

i = 0

while len(newList) > i:
    print(i + 1, newList[i])
    i += 1

newList = ["яблоко", "банан", "киви", "арбуз"]

print('1.', newList[0])
print('2.', newList[1])
print('3.', newList[2])
print('4.', newList[3])

newList = ["яблоко", "банан", "киви", "арбуз"]

listLength = len(newList)

for i in range(listLength):
    print(str(i + 1) + '. ' + '{}'.format(newList[i]))


# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

spisok_1 = {1, 33, 45, "привет", 15.4, "мир"}
spisok_2 = {45, "мир", "осталось", 12, 33, 1}

spisok_3 = spisok_2 - spisok_1
print(list(spisok_3))

# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

lessonList = [1, 22, 13, 14, 95, 11, 78, 15, 64]

newList = []

lessonVar = len(lessonList)

for i in range(lessonVar):
    if lessonList[i] % 2 == 0:
        newList.append(lessonList[i] / 4)
    else:
        newList.append(lessonList[i] * 2)

print(newList)

