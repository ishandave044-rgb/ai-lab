board = [" "]*9

def print_board():
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])

def check_win(player):
    wins = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
    return any(board[a]==board[b]==board[c]==player for a,b,c in wins)

player = "X"

for _ in range(9):
    print_board()
    pos = int(input(f"Player {player}, choose (1-9): "))
    board[pos-1] = player

    if check_win(player):
        print_board()
        print("Player", player, "Wins!")
        break

    player = "O" if player == "X" else "X"
