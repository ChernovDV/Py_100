import random
import time

map_ = [i for i in range(1, 10)]

VICTORY = (
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    (0, 4, 8),
    (2, 4, 6)
)

# Функция для создания поля игры 3x3
def print_map():
    for i in range(3):
        print(f'| {map_[i * 3]} | {map_[i * 3 + 1]} | {map_[i * 3 + 2]} |')

# Функция проверяет вводимые значения через try / except
def check_number(s):
    try:
        number = int(s)
        if number in map_:
            return number
        else:
            print('Неправильная позиция или место занято!')
    except TypeError:
        print('Вы ввели не число')
    return -1

# Функция для отображения символа игрока в выбранной ячейке X/Y
def step_in_map(n, symb):
    ind = map_.index(n)
    map_[ind] = symb

# Функция проверяет может ли компьютер или человек выйграть в следующем ходе
def win_(symb):
    s = ''
    for line in VICTORY:
        if map_[line[0]] == symb and map_[line[1]] == symb and isinstance(map_[line[2]], int):
            s = map_[line[2]]
        elif map_[line[1]] == symb and map_[line[2]] == symb and isinstance(map_[line[0]], int):
            s = map_[line[0]]
        elif map_[line[0]] == symb and map_[line[2]] == symb and isinstance(map_[line[1]], int):
            s = map_[line[1]]
    return s

# Функция ищет для компьютера ряд где уже стоит 0
def zero_():
    s = ''
    for line in VICTORY:
        if map_[line[0]] == 0 and isinstance(map_[line[1]], int) and isinstance(map_[line[2]], int):
            s = map_[line[1]]
        elif map_[line[1]] == 0 and isinstance(map_[line[0]], int) and isinstance(map_[line[2]], int):
            s = map_[line[2]]
        elif map_[line[2]] == 0 and isinstance(map_[line[0]], int) and isinstance(map_[line[1]], int):
            s = map_[line[1]]
    return s

# Функция описывает алгоритм игры компьютера
def ai_step():
    s = ''
    # 1. Если компьютер может выиграть в следующем ходе, он делает это.
    if win_('0'):
        s = win_('0')
    # 2. Если человек может выиграть в следующем ходе, компьютер блокирует его.
    elif win_('X'):
        s = win_('X')
    # 3. Если нет таких вариантов, ищет ряд где уже стоит  0.
    elif zero_():
        s = zero_()
    # 4. Если предыдущие условия не выполняются, компьютер выбирает любую доступную клетку.
    else:
        new_cell = [cell for cell in map_ if isinstance(cell, int)]
        s = random.choice(new_cell)
    return s

# Функция описывает варианты победы в игре
def get_result():
    s = ''
    for line in VICTORY:
        if map_[line[0]] == 'X' and map_[line[1]] == 'X' and map_[line[2]] == 'X':
            s = 'X'
        elif map_[line[0]] == '0' and map_[line[1]] == '0' and map_[line[2]] == '0':
            s = '0'
    return s

# Функция запускает цикл игры
def game():
    name = input('Введи свое имя: ')
    is_human = True
    count_ = 0
    while True:
        count_ += 1
        print_map()
        if is_human:
            s = input(f'{name}, введи номер клетки: ')
            number = check_number(s)
            if number == -1:
                continue
            step_in_map(number, 'X')
            is_human = False
        else:
            print('Ход компьютера!')
            time.sleep(1)
            number = ai_step()
            step_in_map(number, '0')
            is_human = True
        win = get_result()
        if win == 'X':
            print(f'{name} победил!')
            break
        elif win == '0':
            print('Компьютер победил!')
            break
        if count_ == 9:
            print('Ничья!')
            break

game()