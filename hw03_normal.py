# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1


def fibonacci(n, m):

    fib_list = [1, 1]

    if n > m:
        print("Ошибка: Начало интервала должно быть меньше конца интервала")
    else:
        for i in range(m):
            fib_list.append(fib_list[i] + fib_list[i + 1])

    return fib_list[n:m]


print(fibonacci(3, 13))

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):

    x = len(origin_list)

    for i in range(0, x - 1):
        for j in range(0, x - i - 1):
            if origin_list[j] > origin_list[j + 1]:
                origin_list[j], origin_list[j + 1] = origin_list[j + 1], origin_list[j]

    return origin_list


print(sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

def my_filter(a, b):

    filter_result = list()

    for i in b:
        if a(i) is True:
            filter_result.append(i)
        else:
            continue
    return filter_result


print((my_filter((lambda x: x > 3), b=[2, 10, -12, 2.5, 20, -11, 4, 4, 0])))


# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

def parallelogram(*args):
    a = []
    for i in args:
        a.append(i)
    a.sort()
    print("Координаты точек: ", a)
    if a[0][0] + a[3][0] == a[1][0] + a[2][0] and a[0][1] + a[3][1] == a[1][1] + a[2][1]:
        return True


a1 = [-3, -2]
a2 = [-4, -7]
a3 = [-9, -8]
a4 = [-8, -3]

print(parallelogram(a1, a2, a3, a4))
