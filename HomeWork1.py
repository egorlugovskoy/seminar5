# Создайте программу для игры с конфетами человек против компьютера.
# Условие задачи: На столе лежит 150 конфет. Играют игрок против компьютера. Первый ход определяется жеребьёвкой.За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход. 
# Подумайте как наделить бота ""интеллектом""

import random

player1 = input('Введите имя игрока: ')
player2 = 'PC'

candys = 150

start_game = random.randint(0, 1)

if start_game:
    player = player1
else:
    player = player2

while candys > 0:

    if player == player1:
        print()
        print(f'Твой ход {player}')
        take = input('Какое количество конфет хочешь взять? >>> ')
        if take.isdigit():
            take = int(take)
            if take < 1 or take > 28:
                print('Давай без этого. от 1 до 28 конфет за раз')
            else:
                candys -= take
                print(f'На столе осталось {candys} конфет')
                if candys > 0:
                    player = player2
        else:
            print()
            print('Кажется кто то не видит где надо выбрать числа на клавиатуре. давай по новой ')
    else:
        if candys <= 28:
            take = candys
            candys -= take
            print()
            print(f'Компьютер взял {take} конфет, на столе осталось {candys} конфет ')
        else:
            if candys % 29 != 0:
                take = candys % 29
            else:
                take = random.randint(1, 28)
            candys = candys - take
            player = player1
            print()
            print(f'Компьютер взял {take} конфет, на столе осталось {candys} конфет ')

print()
if player == player1:
    print(f'Победил игрок {player}')
else:
    print(f'Победил {player}')