
board = [" " for _ in range(9)]

def print_board():
    for i in range(3):
        print(" | ".join(board[i*3:(i+1)*3]))
        if i < 2:
            print("-" * 5)

def check_winner(player):
    win_positions = [
        (0,1,2),(3,4,5),(6,7,8),
        (0,3,6),(1,4,7),(2,5,8),
        (0,4,8),(2,4,6)
    ]
    for combo in win_positions:
        if all(board[pos] == player for pos in combo):
            return True
    return False

def is_draw():
    return " " not in board

def ai_move():
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            return

while True:
    print_board()

    try:
        move = int(input("Enter your move (1-9): ")) - 1
    except ValueError:
        print("Enter a valid number!")
        continue

    if move < 0 or move > 8 or board[move] != " ":
        print("Invalid move! Try again.")
        continue

    board[move] = "X"

    if check_winner("X"):
        print_board()
        print("You Win!")
        break

    if is_draw():
        print_board()
        print("It's a Draw!")
        break

    ai_move()

    if check_winner("O"):
        print_board()
        print("AI Wins!")
        break

    if is_draw():
        print_board()
        print("It's a Draw!")
        break
