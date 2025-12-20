from game import Connect4
from AI import Connect4AI

def game_loop():
    """
    Game loop for Connect4 with AI opponent.
    """

    game = Connect4()
    player_piece = input("Choose X or O: ").upper()
    ai_depth = int(input("Choose AI depth: "))
    ai_time_limit = int(input("Choose AI time limit (seconds): "))
    ai_piece = "O" if player_piece == "X" else "X"
    ai_player = Connect4AI(ai_piece, depth=ai_depth, time_limit_seconds=ai_time_limit)
    current_player = ai_piece if ai_piece == "X" else player_piece

    while True:

        game.print_board()
        if current_player == ai_piece:
            column = ai_player.best_move(game)
            row = game.drop_piece(column, ai_piece)
            last_move = (row, column)
            print(f"AI chooses column {column + 1}")

        else:
            column = int(input("Player: Enter column (1-7): "))
            if column - 1 not in game.get_valid_moves():
                print("Invalid move. Try again.")
                continue
            else:
                row = game.drop_piece(column - 1, player_piece)
                last_move = (row, column - 1)

        if game.four_in_a_row(current_player, last_move):
            game.print_board()
            print(f"Player {current_player} wins")
            break

        if game.is_full():
            game.print_board()
            print("Game over: No winner")
            break

        current_player = ai_piece if current_player != ai_piece else player_piece

if __name__ == "__main__":
    game_loop()
