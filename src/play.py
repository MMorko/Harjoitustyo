from game import Connect4
from AI import Connect4AI

#Tekoäly puuttuu, toimii pelaaja vastaan pelaaja
def game_loop():
    game = Connect4()

    current_player = "X" 
    while True:
        game.print_board()
        if current_player == "X":
            column = int(input("Player X: Enter column (1-7): "))
            if not game.drop_piece(column - 1, current_player):
                print("Column full")
                continue
        else:
            column = int(input("Player O: Enter column (1-7): "))
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
        
        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    game_loop()