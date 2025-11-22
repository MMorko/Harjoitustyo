class Connect4:
    def __init__(self):
        self.rows = 6
        self.columns = 7
        self.board = [["_" for _ in range(self.columns)] for _ in range(self.rows)]

    def drop_piece(self, column, piece):
        for row in reversed(range(self.rows)):
            if self.board[row][column] == "_":
                self.board[row][column] = piece
                return True
        return False

    def is_full(self):
        for col in range(self.columns):
            if self.board[0][col] == "_":
                return False
        return True
    
    def print_board(self):
        for row in self.board:
            print(" ".join(row))

    def four_in_a_row(self, piece):
        for r in range(self.rows):
            for c in range(self.columns - 3):
                if all(self.board[r][c + i] == piece for i in range(4)):
                    return True
        for c in range(self.columns):
            for r in range(self.rows - 3):
                if all(self.board[r + i][c] == piece for i in range(4)):
                    return True
        for r in range(self.rows - 3):
            for c in range(self.columns - 3):
                if all(self.board[r + i][c + i] == piece for i in range(4)):
                    return True
        for r in range(3, self.rows):
            for c in range(self.columns - 3):
                if all(self.board[r - i][c + i] == piece for i in range(4)):
                    return True
        return False
    
    def get_board(self):
        return self.board
    
    def get_valid_moves(self):
        valid_moves = []
        for col in range(self.columns):
            if self.board[0][col] == "_":
                valid_moves.append(col)
        return valid_moves