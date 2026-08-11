"""
Tic Tac Toe - Player vs Computer (Medium difficulty)

Medium AI logic:
1. Win if possible
2. Block opponent's win if possible
3. Otherwise pick a random available move (no deep lookahead)
"""

import random

BOARD_SIZE = 9
HUMAN = "X"
AI = "O"
EMPTY = " "

WIN_COMBOS = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
    (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
    (0, 4, 8), (2, 4, 6),             # diagonals
]


def print_board(board):
    print()
    for row in range(3):
        cells = board[row * 3:row * 3 + 3]
        print(" " + " | ".join(cells))
        if row < 2:
            print("---+---+---")
    print()


def available_moves(board):
    return [i for i, cell in enumerate(board) if cell == EMPTY]


def check_winner(board, player):
    return any(all(board[i] == player for i in combo) for combo in WIN_COMBOS)


def is_full(board):
    return EMPTY not in board


def find_winning_move(board, player):
    for move in available_moves(board):
        board[move] = player
        if check_winner(board, player):
            board[move] = EMPTY
            return move
        board[move] = EMPTY
    return None


def ai_move(board):
    # 1. Try to win
    move = find_winning_move(board, AI)
    if move is not None:
        return move

    # 2. Block human's win
    move = find_winning_move(board, HUMAN)
    if move is not None:
        return move

    # 3. Take center if free
    if board[4] == EMPTY:
        return 4

    # 4. Take a random corner
    corners = [i for i in (0, 2, 6, 8) if board[i] == EMPTY]
    if corners:
        return random.choice(corners)

    # 5. Otherwise random available move
    return random.choice(available_moves(board))


def get_human_move(board):
    while True:
        raw = input(f"Your move ({HUMAN}) - enter position 1-9: ").strip()
        if not raw.isdigit():
            print("Please enter a number between 1 and 9.")
            continue
        pos = int(raw) - 1
        if pos < 0 or pos >= BOARD_SIZE:
            print("Please enter a number between 1 and 9.")
            continue
        if board[pos] != EMPTY:
            print("That spot is already taken.")
            continue
        return pos


def play_game():
    board = [EMPTY] * BOARD_SIZE
    print("Welcome to Tic Tac Toe!")
    print("You are X, computer is O.")
    print("Positions are numbered 1-9, left to right, top to bottom.")
    print_board([str(i + 1) for i in range(BOARD_SIZE)])

    current = HUMAN
    while True:
        if current == HUMAN:
            move = get_human_move(board)
            board[move] = HUMAN
        else:
            print("Computer is thinking...")
            move = ai_move(board)
            board[move] = AI

        print_board(board)

        if check_winner(board, current):
            if current == HUMAN:
                print("You win! 🎉")
            else:
                print("Computer wins!")
            break

        if is_full(board):
            print("It's a draw!")
            break

        current = AI if current == HUMAN else HUMAN


def main():
    while True:
        play_game()
        again = input("Play again? (y/n): ").strip().lower()
        if again != "y":
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()