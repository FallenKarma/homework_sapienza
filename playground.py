import copy

def play_recursively(board, player, free_spaces,R):
    for row in board:
      print (row)
    print("free:",free_spaces)
    next_player = "W" if player == "B" else "B"
    keepgoing = False
    if not free_spaces:
        check_win_draw(board,R)
    else:
        for space in free_spaces:
            taken_pawns = check_surround(board, space, player)
            if taken_pawns:
                taken_pawns.append(space)
                keepgoing = True
                new_free_spaces = [el for el in free_spaces if el != space]
                # print(new_free_spaces)
                play_recursively(
                    take_over(board, player, taken_pawns), next_player, new_free_spaces,R)
            # else:
            #     R=check_win_draw(board,R)
        if not keepgoing:
          R=check_win_draw(board,R)
def take_over(board, player, spots):
    updated_board = copy.deepcopy(board)
    #updated_board=[row for row in board]
    for spot in spots:
        updated_board[spot[0]][spot[1]] = player
    return updated_board


def check_surround(board, spot, round_player):
    opponent = "W" if round_player == "B" else "B"
    # print(board,spot,round_player,opponent)
    h = len(board)
    w = len(board[1])
    r, c = spot[0], spot[1]
    taken_pawns = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            if r+i >= 0 and r+i < h and c+j >= 0 and c+j < w:
                if board[r+i][c+j] == opponent:
                    #print("vai")
                    taken_pawns.append((r+i, c+j))
    #print(taken_pawns, "\n")
    return taken_pawns


def check_win_draw(board,R):
    blacks = sum(i == "B" for row in board for i in row)
    whites = sum(i == "W" for row in board for i in row)
    if blacks > whites:
        R[0]+=1
        print("Nero vince!",R)
    elif whites > blacks:
        R[1]+=1
        print("Bianco vince!",R)
    else:
        R[2]+=1
        print("Pareggio!",R)
    return R

board = [['.', '.', 'W', 'W'], ['.', '.', 'B', 'B'],
         ['W', 'W', 'W', 'B'], ['W', 'B', 'B', 'W']]
board2 = [['.', '.', '.', 'W'], ['.', 'B', 'W', 'B'],
          ['.', 'W', 'B', 'W'], ['W', 'B', 'W', 'B']]
board3 = [['.', 'B', '.', '.'], ['.', 'B', 'W', 'W'],
          ['W', 'W', 'B', '.'], ['.', '.', 'B', '.']]
board5 = [['W', 'W', 'B', 'W', 'W'], ['B', 'B', 'B', 'W', 'B'], [
    '.', 'B', '.', '.', 'B'], ['W', 'B', '.', 'B', 'W'], ['W', 'B', 'B', 'W', '.']]
board9 = [["B"], ["."], ["."], ["."], ["."], ["."], ["."], ["W"], ["."], ["."]]
board6=[['B', 'B', 'B', 'B', 'B', 'B'], ['W', '.', 'B', 'B', '.', 'B'], ['.', 'B', 'B', 'W', 'B', 'W'], ['B', 'B', 'W', 'W', 'W', '.'], ['W', '.', 'W', 'B', '.', 'W'], ['W', 'W', 'W', 'W', 'W', 'W']]
tryb = [[".", "."], ["W", "W"]]
b1 = [[".", "B", "B"], ["W", "W", "W"], [".", "B", "B"]]
b8=[['W', 'B', 'W', 'B', 'B', 'W', 'W', 'B'], ['B', '.', 'W', 'B', 'B', 'W', 'W', 'W'], ['B', 'W', '.', 'B', 'B', 'W', 'B', 'W'], ['B', '.', '.', '.', 'B', 'B', 'W', 'W'], ['W', 'B', 'B', 'B', 'W', 'W', 'W', 'W'], ['B', 'W', 'W', 'B', 'W', 'B', 'W', '.'], ['B', 'W', 'W', 'B', 'W', 'B', 'B', 'B'], ['W', '.', 'W', 'B', 'W', 'W', 'B', 'W']]
free_spaces = list((i, j) for i, row in enumerate(b8)
                   for j, value in enumerate(row) if value == ".")
play_recursively(b8, "B", free_spaces,[0,0,0])




