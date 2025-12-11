import unittest
from game import Connect4

class TestConnect4(unittest.TestCase):
    """
    Connect4 game tests.
    """
    def setUp(self):
        self.game = Connect4()

    def test_initial_board_empty(self):
        """
        Test that the initial board is empty.
        """
        for row in self.game.board:
            for cell in row:
                self.assertEqual(cell, "_")

    def test_make_move(self):
        """
        Test for making a move.
        """
        self.game.drop_piece(0, "X")
        self.assertEqual(self.game.board[5][0], "X")

    def test_full_column(self):
        """
        Test for dropping a piece in a full column.
        """
        for _ in range(self.game.rows):
            self.game.drop_piece(0, "X")
        self.assertEqual(-1, self.game.drop_piece(0, "O"))

    def test_is_full(self):
        """
        Test for checking if the board is full.
        """
        self.assertFalse(self.game.is_full())

        for col in range(self.game.columns):
            for _ in range(self.game.rows):
                self.game.drop_piece(col, "X")
        self.assertTrue(self.game.is_full())

    def test_print_board(self):
        """
        Test for printing the board.
        """
        from io import StringIO
        import sys

        captured_output = StringIO()
        sys.stdout = captured_output
        self.game.print_board()
        sys.stdout = sys.__stdout__

        expected_output = "\n".join(["_ _ _ _ _ _ _"] * self.game.rows) + "\n"
        self.assertEqual(captured_output.getvalue(), expected_output)

    def test_horizontal_win(self):
        """
        Test for horizontal win.
        """
        for col in range(4):
            self.game.drop_piece(col, "X")
        self.assertTrue(self.game.four_in_a_row("X"))

    def test_vertical_win(self):
        """
        Test for vertical win.
        """
        for _ in range(4):
            self.game.drop_piece(0, "O")
        self.assertTrue(self.game.four_in_a_row("O"))

    def test_left_diagonal_win(self):
        """
        Test for left diagonal win.
        """
        for col in range(4):
            for _ in range(col):
                self.game.drop_piece(col, "X")
            self.game.drop_piece(col, "O")
        self.assertTrue(self.game.four_in_a_row("O"))

    def test_right_diagonal_win(self):
        """
        Test for right diagonal win.
        """
        for col in range(4):
            for _ in range(3 - col):
                self.game.drop_piece(col, "O")
            self.game.drop_piece(col, "X")
        self.assertTrue(self.game.four_in_a_row("X"))

    def test_no_win(self):
        """
        Test for no win.
        """
        self.game.drop_piece(0, "X")
        self.game.drop_piece(1, "O")
        self.game.drop_piece(2, "X")
        self.game.drop_piece(3, "O")
        self.assertFalse(self.game.four_in_a_row("X"))
        self.assertFalse(self.game.four_in_a_row("O"))

    def test_get_valid_moves(self):
        """
        Test for getting valid moves.
        """
        valid_moves = self.game.get_valid_moves()
        self.assertEqual(len(valid_moves), 7)

        for _ in range(self.game.rows):
            self.game.drop_piece(0, "X")

        valid_moves = self.game.get_valid_moves()
        self.assertEqual(len(valid_moves), 6)

    def test_last_move_win_detection(self):
        """
        Test for win detection using last_move parameter.
        """
        for col in range(3):
            self.game.drop_piece(col, "X")
        row = self.game.drop_piece(3, "X")
        self.assertTrue(self.game.four_in_a_row("X", last_move=(row, 3)))
