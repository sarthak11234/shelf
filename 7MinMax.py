


import math


board = [" " for _ in range(9)]



def print_board():
    for i in range(0, 9, 3):
        print("|".join(board[i:i+3]))
        if i < 6:
            print("---------")
    print()



def check_winner():

    winning_positions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]

    for a, b, c in winning_positions:
        if board[a] == board[b] == board[c] != " ":
            return board[a]

    if " " not in board:
        return "Draw"

    return None


# Minimax algorithm
def minimax(is_maximizing):

    result = check_winner()

    if result == "X":
        return -1

    if result == "O":
        return 1

    if result == "Draw":
        return 0

    if is_maximizing:

        best_score = -math.inf

        for i in range(9):
            if board[i] == " ":

                board[i] = "O"

                score = minimax(False)

                board[i] = " "

                best_score = max(best_score, score)

        return best_score

    else:

        best_score = math.inf

        for i in range(9):
            if board[i] == " ":

                board[i] = "X"

                score = minimax(True)

                board[i] = " "

                best_score = min(best_score, score)

        return best_score



def ai_move():

    best_score = -math.inf
    best_move = None

    for i in range(9):

        if board[i] == " ":

            board[i] = "O"

            score = minimax(False)

            board[i] = " "

            if score > best_score:
                best_score = score
                best_move = i

    if best_move is not None:
        board[best_move] = "O"



def play_game():

    print("TIC TAC TOE - Minimax AI")
    print("You are X and AI is O\n")

    print("Position numbers:")
    print("0 | 1 | 2")
    print("---------")
    print("3 | 4 | 5")
    print("---------")
    print("6 | 7 | 8\n")

    print_board()

    while True:

   
        try:
            move = int(input("Enter your position (0-8): "))

            if move < 0 or move > 8 or board[move] != " ":
                print("Invalid move! Try again.")
                continue

        except ValueError:
            print("Enter a valid number!")
            continue

        board[move] = "X"

        print("\nAfter your move:")
        print_board()

        result = check_winner()

        if result:
            break

   
        print("AI is thinking...")
        ai_move()

        print("\nAfter AI move:")
        print_board()

        result = check_winner()

        if result:
            break

    if result == "Draw":
        print("Game Draw!")

    else:
        print(result, "wins!")



play_game()
