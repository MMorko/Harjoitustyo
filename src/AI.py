import time

class Connect4AI:
    """
    Connect4 AI player using Minimax with alpha-beta pruning and time constraints.
    """
    def __init__(self, piece, depth, time_limit_seconds=4):
        self.piece = piece
        self.depth = depth
        self.opponent = "O" if piece == "X" else "X"
        self.memory = {}
        self.time_limit_seconds = time_limit_seconds
        self._start_time = None

    def minimax(self, game, depth, maximizing, alpha, beta):
        """
        Minimax algorithm with alpha-beta pruning and time limit.
        
        :param game: Current game state
        :param depth: Current depth in the game tree
        :param maximizing: True/false indicating if maximizing or not
        :param alpha: Alpha value for alpha-beta pruning
        :param beta: Beta value for alpha-beta pruning

        Returns a tuple score, column where score is the evaluated score and column is the best move.
        """
        if self._start_time and (time.time() - self._start_time) > self.time_limit_seconds:
            return None, None

        if game.four_in_a_row(self.opponent):
                return -100000 - depth, None
        if game.four_in_a_row(self.piece):
                return 100000 + depth, None
        if game.is_full():
            return 0, None
        if depth == 0:
            return self.evaluate_board(game, self.piece), None

        board_key = tuple(tuple(row) for row in game.board)
        valid_moves = game.get_valid_moves()

        memory_key = (board_key, maximizing)
        best_colm = self.memory.get(memory_key)
        if best_colm in valid_moves:
            valid_moves.remove(best_colm)
            valid_moves.insert(0, best_colm)

        if maximizing:
            best_score = -100000
            best_col = None

            for col in valid_moves:
                row = game.drop_piece(col, self.piece)
                if row == -1:
                    continue

                score, _ = self.minimax(game, depth - 1, False, alpha, beta)
                game.remove_piece(row, col)

                if score is None:
                    return None, None

                if score > best_score:
                    best_score = score
                    best_col = col

                alpha = max(alpha, best_score)
                if beta <= alpha:
                    break

            self.memory[memory_key] = best_col
            return best_score, best_col

        else:
            best_score = 100000
            best_col = None

            for col in valid_moves:
                row = game.drop_piece(col, self.opponent)
                if row == -1:
                    continue

                score, _ = self.minimax(game, depth - 1, True, alpha, beta)
                game.remove_piece(row, col)

                if score is None:
                    return None, None

                if score < best_score:
                    best_score = score
                    best_col = col

                beta = min(beta, best_score)
                if beta <= alpha:
                    break

            self.memory[memory_key] = best_col
            return best_score, best_col

    def best_move(self, game):
        """
        Method for calling minimax and getting the best move.

        :param game: Current game state

        Returns the best move.
        """
        self.memory = {}
        self._start_time = time.time()

        for col in game.get_valid_moves():
            row = game.drop_piece(col, self.piece)
            if row != -1:
                if game.four_in_a_row(self.piece, last_move=(row, col)):
                    game.remove_piece(row, col)
                    return col
                game.remove_piece(row, col)

        for col in game.get_valid_moves():
            row = game.drop_piece(col, self.opponent)
            if row != -1:
                if game.four_in_a_row(self.opponent, last_move=(row, col)):
                    game.remove_piece(row, col)
                    return col
                game.remove_piece(row, col)

        best_move = None

        for depth in range(1, self.depth + 1):
            _, move = self.minimax(game, depth, True, -100000, 100000)
            if move is not None:
                best_move = move
            else:
                break

        return best_move

    def evaluate_board(self, game, piece):
        """
        Docstring for evaluate_board
        
        :param game: Current game state
        :param piece: Piece to evaluate for

        Returns the evaluated score of the board.
        """
        score = 0
        board = game.get_board()
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
        """
        Evaluates a window of four cells.

        :param window: List of four cells
        :param piece: Piece to evaluate for

        Returns the score of the window.
        """
        score = 0

        count_own = window.count(piece)
        count_empty = window.count("_")

        if count_own == 3 and count_empty == 1:
            score += 1000
        elif count_own == 2 and count_empty == 2:
            score += 20
        elif count_own == 1 and count_empty == 3:
            score += 1
        elif count_own == 0 and count_empty == 1:
            score -= 1000
        elif count_own == 0 and count_empty == 2:
            score -= 25
        elif count_own == 0 and count_empty == 1:
            score -=1

        return score