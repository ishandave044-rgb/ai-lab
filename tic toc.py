board = [" "] * 9

# Board print karne ka easy function
def show():
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])

# Winning check (simple)
def win(p):
    c = board
    lines = [
        (0,1,2), (3,4,5), (6,7,8),
        (0,3,6), (1,4,7), (2,5,8),
        (0,4,8), (2,4,6)
    ]
    for a,b,c in lines:
        if board[a] == board[b] == board[c] == p:
            return True
    return False


player = "X"

for turn in range(9):
    show()
    
    pos = int(input(f"Player {player}, choose (1-9): "))
    pos -= 1   # converting to 0–8 index
    
    if board[pos] != " ":
        print("Already filled! Try again.")
        continue

    board[pos] = player

    if win(player):
        show()
        print("Player", player, "wins!")
        break

    # Switch player
    player = "O" if player == "X" else "X"

else:
    show()
    print("Match Draw 😊")
