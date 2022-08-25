from random import randint

# Доска для изображения кораблей
HIDDEN_BOARD = [[" "] * 6 for x in range(6)]
# Доска для изображения попаданий и промахов
GUESS_BOARD = [[" "] * 6 for i in range(6)]


def print_board(board):
    print("  A B C D E F")
    row_number = 1
    for row in board:
        print("%d|%s|" % (row_number, "|".join(row)))
        row_number += 1


# Присваивание букв к значениям для column = input
letters_to_numbers = {
    'A': 0,
    'B': 1,
    'C': 2,
    'D': 3,
    'E': 4,
    'F': 5,
}


# Создадим 3 случайных корабля
def create_ships(board):
    play_or_quit = str(input("Добро пожаловать в Морской бой, моряк-программист! \n"
                             "Чтобы начать игру, напишите play или exit, чтобы выйти: "))
    if play_or_quit == "play":
        for ship in range(3):
            ship_row, ship_column = randint(0, 4), randint(0, 4)
            while board[ship_row][ship_column] == "X":
                ship_row, ship_column = get_ship_location()
            board[ship_row][ship_column] = "X"
    elif play_or_quit == "exit":
        quit()
    else:
        raise ValueError("Не было введено соответсвующее значение, завершаем работу!")


def get_ship_location():
    row = input("Укажите строку корабля: ").upper()
    while row not in "123456":
        print('Неверное значение, введите верное значение в диапазоне от 1 до 6')
        row = input("Укажите строку корабля: ").upper()
    column = input("Укажите столб корабля: ").upper()
    while column not in "ABCDEF":
        print('Неверное значение, введите верное значение в диапазоне от A до F')
        column = input("Укажите столб корабля: ").upper()
    return int(row) - 1, letters_to_numbers[column]


# Проверка, не все ли корабли поражены
def count_hit_ships(board):
    count = 0
    for row in board:
        for column in row:
            if column == "X":
                count += 1
    return count


if __name__ == "__main__":
    create_ships(HIDDEN_BOARD)
    turns = 24
    while turns > 0:
        print('Угадайте, где находятся корабли')
        print_board(GUESS_BOARD)
        row, column = get_ship_location()
        if GUESS_BOARD[row][column] == "-":
            print("Вы уже угадали эту ячейку.")
        elif HIDDEN_BOARD[row][column] == "X":
            print("Удар")
            GUESS_BOARD[row][column] = "X"
            turns -= 1
        else:
            print("Промах!")
            GUESS_BOARD[row][column] = "-"
            turns -= 1
        if count_hit_ships(GUESS_BOARD) == 3:
            print("Победа!")
            break
        print("Осталось " + str(turns) + " ходов")
        if turns == 0:
            print("Ходов не осталось, игра проиграна!")
