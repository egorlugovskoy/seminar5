#Создайте программу для игры в ""Крестики-нолики"".

cells = list(range(1,10))

def draw_cells(cells):
    print ("------------------")
    for i in range(3):
        print ("||", cells[0+i*3], "||", cells[1+i*3], "||", cells[2+i*3], "||")
        print ("------------------")

def take_input(player_token):
    valid = False
    while not valid:
        player_answer = input("Куда поставим " + player_token+"? ")
        try:
            player_answer = int(player_answer)
        except:
            print ("Некорректный ввод. Вы уверены, что ввели число?")
            continue
        if player_answer >= 1 and player_answer <= 9:
            if (str(cells[player_answer-1]) not in "XO"):
                cells[player_answer-1] = player_token
                valid = True
            else:
                print ("Эта клеточка уже занята")
        else:
            print ("Некорректный ввод. Введите число от 1 до 9 чтобы походить.")

def check_win(cells):
    win_coord = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for each in win_coord:
        if cells[each[0]] == cells[each[1]] == cells[each[2]]:
            return cells[each[0]]
    return False

def main(cells):
    counter = 0
    win = False
    while not win:
        draw_cells(cells)
        if counter % 2 == 0:
            take_input("X")
        else:
            take_input("O")
        counter += 1
        if counter > 4:
            tmp = check_win(cells)
            if tmp:
                print (tmp, "выиграл!")
                win = True
                break
        if counter == 9:
            print ("Ничья!")
            break
    draw_cells(cells)

main(cells)