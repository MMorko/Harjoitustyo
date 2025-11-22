from game import Connect4
from AI import Connect4AI

def game_loop():
    game = Connect4()
    player_piece = input("Choose X or O: ").upper()
    ai_piece = "O" if player_piece == "X" else "X"
    ai_player = Connect4AI(ai_piece, depth=6)
    current_player = ai_piece if ai_piece == "X" else player_piece

    while True:

        game.print_board()
        if current_player == ai_piece:
            column = ai_player.best_move(game)
            game.drop_piece(column, ai_piece)
            print(f"AI chooses column {column + 1}")

        else:
            column = int(input("Player: Enter column (1-7): "))
            if not game.drop_piece(column - 1, current_player):
                print("Column full")
                continue

        if game.is_full():
            game.print_board()
            print("Game over: No winner")
            break
        
        if game.four_in_a_row(current_player):
            game.print_board()
            print(f"Player {current_player} wins")
            break
        
        current_player = ai_piece if current_player != ai_piece else player_piece

if __name__ == "__main__":
    game_loop()