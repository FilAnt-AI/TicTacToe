import pygame

white = (250, 250, 250)
display_width = 600
display_height = 600
gameDisplay = pygame.display.set_mode((display_width, display_height))
xImg = pygame.image.load('xpng.png')
oImg = pygame.image.load('o_png.png')
planszaImg = pygame.image.load('332570.png')
minimax_array = []

for i in range(0, 10 ** 5): minimax_array.append(2)


def prtBoard(x):
    print(x[0], " | ", x[1], " | ", x[2])
    print("-------------")
    print(x[3], " | ", x[4], " | ", x[5])
    print("-------------")
    print(x[6], " | ", x[7], " | ", x[8])


def empty_squares(board):
    empty_idx = []
    for i in range(0, 9):
        if board[i] == 0: empty_idx.append(i)
    return empty_idx


def decode_number(board_number):
    board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    number = board_number
    i = 0
    while (number > 0):
        board[i] = number % 3
        number //= 3
        i += 1
    return board


def code_board(board):
    result = 0
    for i in range(0, 9):
        result += board[i] * (3 ** i)
    return result


def if_win(board):
    if board[0] == board[1] and board[1] == board[2] and board[0] != 0:
        if board[0] == 2:
            return 1
        else:
            return -1

    if board[3] == board[4] and board[4] == board[5] and board[3] != 0:
        if board[3] == 2:
            return 1
        else:
            return -1

    if board[6] == board[7] and board[7] == board[8] and board[6] != 0:
        if board[6] == 2:
            return 1
        else:
            return -1

    if board[0] == board[3] and board[3] == board[6] and board[0] != 0:
        if board[0] == 2:
            return 1
        else:
            return -1

    if board[2] == board[5] and board[5] == board[8] and board[2] != 0:
        if board[2] == 2:
            return 1
        else:
            return -1

    if board[1] == board[4] and board[4] == board[7] and board[1] != 0:
        if board[1] == 2:
            return 1
        else:
            return -1

    if board[0] == board[4] and board[0] == board[8] and board[0] != 0:
        if board[0] == 2:
            return 1
        else:
            return -1

    if board[2] == board[4] and board[2] == board[6] and board[2] != 0:
        if board[2] == 2:
            return 1
        else:
            return -1

    for i in range(0, 9):
        if board[i] == 0:
            return 2

    return 0


def generating_boards(board_number, move):
    if if_win(decode_number(board_number)) < 2:
        minimax_array[board_number] = if_win(decode_number(board_number))
        return
    minimax_neighbours = []
    empty_idx = empty_squares(decode_number(board_number))
    for idx in empty_idx:
        if move % 2 == 0:
            u = board_number + 2 * (3 ** idx)
        else:
            u = board_number + (3 ** idx)
        if minimax_array[u] == 2: generating_boards(u, move + 1)
        minimax_neighbours.append(minimax_array[u])
    if move % 2 == 0:
        minimax_array[board_number] = max(minimax_neighbours)
    else:
        minimax_array[board_number] = min(minimax_neighbours)


def best_move(board_number, move):
    minimax_neighbours = []
    neighbours = []
    empty_idx = empty_squares(decode_number(board_number))
    for idx in empty_idx:
        if move % 2 == 0:
            u = board_number + 2 * (3 ** idx)
        else:
            u = board_number + (3 ** idx)
        minimax_neighbours.append(minimax_array[u])
        neighbours.append(u)
    if move % 2 == 0:
        return neighbours[minimax_neighbours.index(max(minimax_neighbours))]
    else:
        return neighbours[minimax_neighbours.index(min(minimax_neighbours))]


def square1(ktory):
    if ktory == 1:
        gameDisplay.blit(xImg, (20, 20))
    elif ktory == 2:
        gameDisplay.blit(oImg, (20, 20))


def square2(ktory):
    if ktory == 1:
        gameDisplay.blit(xImg, (225, 20))
    elif ktory == 2:
        gameDisplay.blit(oImg, (225, 20))


def square3(ktory):
    if ktory == 1:
        gameDisplay.blit(xImg, (420, 20))
    elif ktory == 2:
        gameDisplay.blit(oImg, (420, 20))


def square4(ktory):
    if ktory == 1:
        gameDisplay.blit(xImg, (20, 230))
    elif ktory == 2:
        gameDisplay.blit(oImg, (20, 230))


def square5(ktory):
    if ktory == 1:
        gameDisplay.blit(xImg, (225, 230))
    elif ktory == 2:
        gameDisplay.blit(oImg, (225, 230))


def square6(ktory):
    if ktory == 1:
        gameDisplay.blit(xImg, (420, 230))
    elif ktory == 2:
        gameDisplay.blit(oImg, (420, 230))


def square7(ktory):
    if ktory == 1:
        gameDisplay.blit(xImg, (20, 420))
    elif ktory == 2:
        gameDisplay.blit(oImg, (20, 420))


def square8(ktory):
    if ktory == 1:
        gameDisplay.blit(xImg, (225, 420))
    elif ktory == 2:
        gameDisplay.blit(oImg, (225, 420))


def square9(ktory):
    if ktory == 1:
        gameDisplay.blit(xImg, (420, 420))
    elif ktory == 2:
        gameDisplay.blit(oImg, (420, 420))


def board():
    gameDisplay.blit(planszaImg, (0, 0))


def gameImage(planszaAkt):
    gameDisplay.fill(white)
    board()
    if planszaAkt[0] == 1:
        square1(1)
    elif planszaAkt[0] == 2:
        square1(2)
    else:
        square1(3)

    if planszaAkt[1] == 1:
        square2(1)
    elif planszaAkt[1] == 2:
        square2(2)
    else:
        square2(3)

    if planszaAkt[2] == 1:
        square3(1)
    elif planszaAkt[2] == 2:
        square3(2)
    else:
        square3(3)

    if planszaAkt[3] == 1:
        square4(1)
    elif planszaAkt[3] == 2:
        square4(2)
    else:
        square4(3)

    if planszaAkt[4] == 1:
        square5(1)
    elif planszaAkt[4] == 2:
        square5(2)
    else:
        square5(3)

    if planszaAkt[5] == 1:
        square6(1)
    elif planszaAkt[5] == 2:
        square6(2)
    else:
        square6(3)

    if planszaAkt[6] == 1:
        square7(1)
    elif planszaAkt[6] == 2:
        square7(2)
    else:
        square7(3)

    if planszaAkt[7] == 1:
        square8(1)
    elif planszaAkt[7] == 2:
        square8(2)
    else:
        square8(3)

    if planszaAkt[8] == 1:
        square9(1)
    elif planszaAkt[8] == 2:
        square9(2)
    else:
        square9(3)


def square_detect(x, y):
    if 0 < x < display_width / 3 and 0 < y < display_height / 3:
        return 0
    elif display_width / 3 < x < 2 * display_width / 3 and 0 < y < display_height / 3:
        return 1
    elif 2 * display_width / 3 < x < display_width and 0 < y < display_height / 3:
        return 2
    elif 0 < x < display_width / 3 and display_height / 3 < y < 2 * display_height / 3:
        return 3
    elif display_width / 3 < x < 2 * display_width / 3 and display_height / 3 < y < 2 * display_height / 3:
        return 4
    elif 2 * display_width / 3 < x < display_width and display_height / 3 < y < 2 * display_height / 3:
        return 5
    elif 0 < x < display_width / 3 and 2 * display_height / 3 < y < display_height:
        return 6
    elif display_width / 3 < x < 2 * display_width / 3 and 2 * display_height / 3 < y < display_height:
        return 7
    elif 2 * display_width / 3 < x < display_width and 2 * display_height / 3 < y < display_height:
        return 8


def game():
    pygame.init()
    crashed = False
    who = 1
    move = 0
    act_board = 0
    ifEnd = False

    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                square_idx = square_detect(mouse[0], mouse[1])
                if decode_number(act_board)[square_idx] == 0 and move % 2 == who and ifEnd == False:
                    act_board += (3 ** square_idx)
                    move += 1

        if move % 2 == who - 1:
            gameImage(decode_number(act_board))
            pygame.display.update()
            pygame.time.wait(300)
            act_board = best_move(act_board, move)
            move += 1

        if if_win(decode_number(act_board)) != 2:
            ifEnd = True

        gameImage(decode_number(act_board))

        mouse = pygame.mouse.get_pos()
        pygame.display.update()



generating_boards(0, 0)
game()
