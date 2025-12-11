import unittest
from AI import Connect4AI
from game import Connect4

class TestConnect4AI(unittest.TestCase):
    """
    Connect4AI tests.
    """
    def setUp(self):
        self.game = Connect4()
        self.ai = Connect4AI(piece="X", depth=10, time_limit_seconds=4)

    def test_ai_finds_winning_move(self):
        """
        Test for finding immediate winning move.
        """
        self.game.board =[
            ["_", "_", "_", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "_", "_", "O"],
            ["_", "_", "_", "_", "_", "_", "O"],
            ["_", "X", "X", "X", "O", "O", "O"],
        ]
        col = self.ai.best_move(self.game)
        self.assertEqual(col, 0)

    def test_ai_blocks_opponent_winning_move(self):
        """
        Test for blocking opponent immediate winning move.
        """
        self.game.board =[
            ["_", "_", "_", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "_", "_", "_"],
            ["_", "O", "O", "O", "X", "X", "X"],
        ]
        col = self.ai.best_move(self.game)
        self.assertEqual(col, 0)

    def test_evaluate_window_own_piece(self):
        """
        Test for evaluating window with own pieces.
        """
        self.assertEqual(self.ai.evaluate_window(["X", "X", "X", "_"], "X"), 1000)
        self.assertEqual(self.ai.evaluate_window(["X", "X", "_", "_"], "X"), 20)
        self.assertEqual(self.ai.evaluate_window(["X", "_", "_", "_"], "X"), 1)
        self.assertEqual(self.ai.evaluate_window(["_", "_", "_", "_"], "X"), 0)

    def test_evaluate_window_opponent_piece(self):
        """
        Test for evaluating window with opponent pieces.
        """
        self.assertEqual(self.ai.evaluate_window(["O", "O", "O", "_"], "X"), -1000)
        self.assertEqual(self.ai.evaluate_window(["O", "O", "_", "_"], "X"), -25)
        self.assertEqual(self.ai.evaluate_window(["O", "_", "_", "_"], "X"), -1)

    def test_evaluate_board(self):
        """
        Test for evaluating the board.
        """
        self.game.board =[
            ["_", "_", "_", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "_", "_", "_"],
            ["X", "_", "_", "_", "_", "_", "_"],
            ["O", "O", "_", "_", "X", "O", "O"],
            ["X", "X", "_", "_", "O", "X", "X"],
        ]
        score = self.ai.evaluate_board(self.game, "X")
        self.assertEqual(score, 14)
