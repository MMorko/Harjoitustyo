class Connect4:
    """
    Connect4 game and its methods.
    """
    def __init__(self):
        self.rows = 6
        self.columns = 7
        self.board = [["_" for _ in range(self.columns)] for _ in range(self.rows)]

    def drop_piece(self, column, piece):
        """
        Drops a piece into given column.

        Params: column (int): The column index (0-6).
                piece (str): The piece to drop ("X" or "O").

        Returns the row where the piece landed or -1 if the column is full.
        """
        for row in reversed(range(self.rows)):
            if self.board[row][column] == "_":
                self.board[row][column] = piece
                return row
        return -1

    def remove_piece(self, row, column):
        """
        Removes a piece from given row and column.
        Params: row (int): The row index.
                column (int): The column index.
        """
        self.board[row][column] = "_"

    def is_full(self):
        """
        Checks if the board is full.

        Returns True if full, False otherwise.
        """
        for col in range(self.columns):
            if self.board[0][col] == "_":
                return False
        return True

    def print_board(self):
        """
        Prints the current state of the board.
        """
        for row in self.board:
            print(" ".join(row))

    def four_in_a_row(self, piece, last_move = None):
        """
        Checks if there are four in a row for the given piece.

        Params: piece (str): The piece to check for ("X" or "O").
                last_move (tuple): Optional (row, column) of the last move made.

        Returns True if there are four in a row, False otherwise.
        """
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
        """
        Returns the current state of the board.
        """
        return self.board

    def get_valid_moves(self):
        """
        Returns a list of valid columns where a piece can be dropped
        in the order of preference.
        """
        order = [3, 4, 2, 5, 1, 6, 0]
        valid_moves = []
        for col in order:
            if self.board[0][col] == "_":
                valid_moves.append(col)
        return valid_moves
