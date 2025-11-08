import unittest
from game import Connect4

class TestConnect4(unittest.TestCase):
    def setUp(self):
        self.game = Connect4()

    def test_initial_board_empty(self):
        for row in self.game.board:
            for cell in row:
                self.assertEqual(cell, "_")

    def test_make_move(self):
        self.game.drop_piece(0, "X")
        self.assertEqual(self.game.board[5][0], "X")

    def test_full_column(self):
        for _ in range(self.game.rows):
            self.game.drop_piece(0, "X")
        self.assertFalse(self.game.drop_piece(0, "O"))

    def test_is_full(self):
        self.assertFalse(self.game.is_full())

        for col in range(self.game.columns):
            for _ in range(self.game.rows):
                self.game.drop_piece(col, "X")
        self.assertTrue(self.game.is_full())

    def test_print_board(self):
        from io import StringIO
        import sys

        captured_output = StringIO()
        sys.stdout = captured_output
        self.game.print_board()
        sys.stdout = sys.__stdout__

        expected_output = "\n".join(["_ _ _ _ _ _ _"] * self.game.rows) + "\n"
        self.assertEqual(captured_output.getvalue(), expected_output)

    def test_horizontal_win(self):
        for col in range(4):
            self.game.drop_piece(col, "X")
        self.assertTrue(self.game.four_in_a_row("X"))

    def test_vertical_win(self):
        for _ in range(4):
            self.game.drop_piece(0, "O")
        self.assertTrue(self.game.four_in_a_row("O"))

    def test_left_diagonal_win(self):
        for col in range(4):
            for _ in range(col):
                self.game.drop_piece(col, "X")
            self.game.drop_piece(col, "O")
        self.assertTrue(self.game.four_in_a_row("O"))

    def test_right_diagonal_win(self):
        for col in range(4):
            for _ in range(3 - col):
                self.game.drop_piece(col, "O")
            self.game.drop_piece(col, "X")
        self.assertTrue(self.game.four_in_a_row("X"))

    def test_no_win(self):
        self.game.drop_piece(0, "X")
        self.game.drop_piece(1, "O")
        self.game.drop_piece(2, "X")
        self.game.drop_piece(3, "O")
        self.assertFalse(self.game.four_in_a_row("X"))
        self.assertFalse(self.game.four_in_a_row("O"))