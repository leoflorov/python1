# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом)
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math


# def my_round(number, ndigits):
#     pass
#
# my_round(2.1234567, 5)

def my_round(number, ndigits):
    number = number*(10*ndigits)+0.41
    number = number // 1
    return number /(10**ndigits)
print(my_round(2.1234567, 5))

# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить


# def lucky_ticket(ticket_number):
#     pass

ticket_number = int(input("Введите номер вашего билета: "))

def lucky_ticket(ticket_number):
    num = str(ticket_number)
    list1 = int(num[:1]) + int(num[1:2])
    list2 = int(num[-1]) + int(num[-2])
    if list1 == list2:
        return True
    else:
        return False

print("Если вернулось True, то билет счастливый!", lucky_ticket(ticket_number))
