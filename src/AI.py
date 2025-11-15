import math
import random
from game import Connect4

class Connect4AI:
    def __init__(self, piece):
        self.piece = piece

    def minimax(self, game):
        best_score = -math.inf
        best_col = []

        for col in range(game.columns):
            if game.board[0][col] == "_":
                game_copy = Connect4()
                game_copy.board = [row[:] for row in game.board]
                game_copy.drop_piece(col, self.piece)
                score = self.evaluate_board(game_copy, self.piece)

                if score > best_score:
                    best_score = score
                    best_col = [col]
                elif score == best_score:
                    best_col.append(col)

        return random.choice(best_col)
    
    def best_move(self, game):
        move = self.minimax(game)
        return move
        
    def evaluate_board(self, game, piece):
        score = 0
        score += self.count_windows(game.get_board(), piece)
        return score 
    
    def count_windows(self, board, piece):
        score = 0
        rows = len(board)
        columns = len(board[0])

        for row in range(rows):
            for col in range(columns - 3):
                window = [board[row][col + i] for i in range(4)]
                score += self.evaluate_window(window, piece)

        for col in range(columns):
            for row in range(rows - 3):
                window = [board[row + i][col] for i in range(4)]
                score += self.evaluate_window(window, piece)

        for row in range(rows - 3):
            for col in range(columns - 3):
                window = [board[row + i][col + i] for i in range(4)]
                score += self.evaluate_window(window, piece)

        for row in range(3, rows):
            for col in range(columns - 3):
                window = [board[row - i][col + i] for i in range(4)]
                score += self.evaluate_window(window, piece)

        return score
    
    def evaluate_window(self, window, piece):
        opp_piece = "O" if piece == "X" else "X"
        score = 0

        count_own = window.count(piece)
        count_opp = window.count(opp_piece)
        count_empty = window.count("_")

        if count_own == 4:
            score += 100000
        elif count_own == 3 and count_empty == 1:
            score += 30
        elif count_own == 2 and count_empty == 2:
            score += 10

        if count_opp == 3 and count_empty == 1:
            score -= 10000
        elif count_opp == 2 and count_empty == 2:
            score -= 10
            
        return score