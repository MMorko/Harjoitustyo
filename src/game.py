class Connect4:
    def __init__(self):
        self.rows = 6
        self.columns = 7
        self.board = [["_" for _ in range(self.columns)] for _ in range(self.rows)]

    def drop_piece(self, column, piece):
        for row in reversed(range(self.rows)):
            if self.board[row][column] == "_":
                self.board[row][column] = piece
                return row
        return -1

    def remove_piece(self, row, column):
        self.board[row][column] = "_"

    def is_full(self):
        for col in range(self.columns):
            if self.board[0][col] == "_":
                return False
        return True

    def print_board(self):
        for row in self.board:
            print(" ".join(row))

    def four_in_a_row(self, piece, last_move = None):
        if last_move is None:
            for row in range(self.rows):
                for col in range(self.columns - 3):
                    if all(self.board[row][col + i] == piece for i in range(4)):
                        return True
            for col in range(self.columns):
                for row in range(self.rows - 3):
                    if all(self.board[row + i][col] == piece for i in range(4)):
                        return True
            for row in range(self.rows - 3):
                for col in range(self.columns - 3):
                    if all(self.board[row + i][col + i] == piece for i in range(4)):
                        return True
            for row in range(3, self.rows):
                for col in range(self.columns - 3):
                    if all(self.board[row - i][col + i] == piece for i in range(4)):
                        return True
            return False
        
        row, col = last_move
        directions = [(0, 1), (1, 0), (1, 1), (1, -1)]

        for dr, dc in directions:
            count = 1

            r, c = row + dr, col + dc
            while 0 <= r < self.rows and 0 <= c < self.columns and self.board[r][c] == piece:
                count += 1
                r += dr
                c += dc

            r, c = row - dr, col - dc
            while 0 <= r < self.rows and 0 <= c < self.columns and self.board[r][c] == piece:
                count += 1
                r -= dr
                c -= dc

            if count >= 4:
                return True
            
        return False
    
    def get_board(self):
        return self.board

    def get_valid_moves(self):
        order = [3, 4, 2, 5, 1, 6, 0]
        valid_moves = []
        for col in order:
            if self.board[0][col] == "_":
                valid_moves.append(col)
        return valid_moves
