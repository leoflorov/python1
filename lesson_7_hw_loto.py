"""
Лото

Правила игры в лото.

Игра ведется с помощью специальных карточек, на которых отмечены числа,
и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр,
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

--------------------------
   9 43 62          74 90
2    27    75 78    82
  41 56 63     76      86
--------------------------
"""
"""
В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается
случайная карточка.

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
    Если цифра есть на карточке - она зачеркивается и игра продолжается.
    Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
    Если цифра есть на карточке - игрок проигрывает и игра завершается.
    Если цифры на карточке нет - игра продолжается.

Побеждает тот, кто первый закроет все числа на своей карточке.

Пример одного хода:

Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
6  7          49    57 58
  14 26     -    78    85
23 33    38    48    71  
--------------------------
-- Карточка компьютера ---
7 87     - 14    11      
     16 49    55 88    77    
  15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать
модуль random: http://docs.python.org/3/library/random.html

"""

import sys
import random


kegs_left = 90
player_1 = 15
player_cpu = 15
kegs = random.sample(range(90), 90)
game_set = random.sample(range(90), 30)
player_1_set = random.sample(game_set, 15)
player_cpu_set = [i for i in game_set if not i in player_1_set]
player_1_field = [player_1_set[:5], player_1_set[5:10], player_1_set[10:]]
player_cpu_field = [player_cpu_set[:5], player_cpu_set[5:10], player_cpu_set[10:]]
for player_1_line in player_1_field:
    player_1_line.sort()
    player_1_line.insert(random.randint(0, 4), ' ')
    player_1_line.insert(random.randint(0, 5), ' ')
    player_1_line.insert(random.randint(0, 6), ' ')
    player_1_line.insert(random.randint(0, 7), ' ')
for player_cpu_line in player_cpu_field:
    player_cpu_line.sort()
    player_cpu_line.insert(random.randint(0, 4), ' ')
    player_cpu_line.insert(random.randint(0, 5), ' ')
    player_cpu_line.insert(random.randint(0, 6), ' ')
    player_cpu_line.insert(random.randint(0, 7), ' ')


def field(p):
    if p == 0:
        print('{:-^26}'.format(' Ваша карточка '))
        for line1 in player_1_field:
            for n1 in line1:
                print('{0:>2}'.format(n1), end=' ')
            print()
        print('{:-^26}\n'.format('-'))
    if p == 1:
        print('{:-^26}'.format(' Карточка компьютера '))
        for line2 in player_cpu_field:
            for n2 in line2:
                print('{0:>2}'.format(n2), end=' ')
            print()
        print('{:-^26}\n'.format('-'))


def player_move():
    a = input('Зачеркнуть цифру? (y/n): ')
    if a == 'y':
        if keg in player_1_set:
            for l in player_1_field:
                try:
                    l.insert(l.index(keg), 'X')
                    l.pop(l.index(keg))
                except ValueError:
                    continue
            print('\nOK')
            return 1
        else:
            print('\nGAME OVER')
            sys.exit()
    if a == 'n':
        if keg in player_1_set:
            print('\nGAME OVER')
            sys.exit()
        else:
            print('\nOK')


def cpu_move():
    if keg in player_cpu_set:
        for i in player_cpu_field:
            try:
                i.insert(i.index(keg), 'X')
                i.pop(i.index(keg))
            except ValueError:
                continue
        return 1


for keg in kegs:
    kegs_left -= 1
    print(f'\nНовый бочонок: {keg} (осталось: {kegs_left})\n')
    field(0)
    field(1)
    if player_move() == 1:
        player_1 -= 1
    if cpu_move() == 1:
        player_cpu -= 1
    if player_1 == 0:
        print('\nYOU WON')
        sys.exit()
    if player_cpu == 0:
        print('\nYOU LOSE')
        sys.exit()
    if kegs_left == 0:
        print('\nGAME OVER')
        sys.exit()


