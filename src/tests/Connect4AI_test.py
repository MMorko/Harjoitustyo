import unittest
from AI import Connect4AI
from game import Connect4
#minimax testi voitto 5 vuoroa syvyydellä 5.
#sama testi kun voitto 3 vuoroa syvyydellä 5.
#best_move testi

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
        score, col, tl = self.ai.best_move(self.game)
        self.assertEqual(score, 100100)

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
        score, col, tl = self.ai.best_move(self.game)
        self.assertEqual(score, -100100)

    def test_evaluate_window_own_piece(self):
        """
        Test for evaluating window with own pieces.
        """
        self.assertEqual(self.ai.evaluate_window(["X", "X", "X", "_"], "X"), 1000)
        self.assertEqual(self.ai.evaluate_window(["X", "_", "_", "X"], "X"), 20)
        self.assertEqual(self.ai.evaluate_window(["_", "_", "X", "_"], "X"), 1)
        self.assertEqual(self.ai.evaluate_window(["_", "_", "_", "_"], "X"), 0)

    def test_evaluate_window_opponent_piece(self):
        """
        Test for evaluating window with opponent pieces.
        """
        self.assertEqual(self.ai.evaluate_window(["O", "_", "O", "O"], "X"), -1000)
        self.assertEqual(self.ai.evaluate_window(["O", "O", "_", "_"], "X"), -25)
        self.assertEqual(self.ai.evaluate_window(["O", "_", "_", "_"], "X"), -1)
        self.assertEqual(self.ai.evaluate_window(["X", "_", "O", "_"], "X"), 0)

    def test_evaluate_board_case_1(self):
        """
        Test for evaluating the board.
        """
        self.game.board = [
            ["_", "_", "_", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "_", "_", "_"],
            ["X", "_", "_", "_", "_", "_", "O"],
            ["O", "O", "_", "_", "X", "O", "O"],
            ["X", "X", "_", "_", "O", "X", "X"],
        ]
        score = self.ai.evaluate_board(self.game, "X")
        self.assertEqual(score, -13)

    def test_evaluate_board_case_2(self):
        """
        Test for evaluating the board.
        """
        self.game.board = [
            ["_", "_", "_", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "_", "_", "_"],
            ["O", "_", "_", "_", "_", "_", "_"],
            ["X", "O", "X", "O", "_", "_", "_"],
            ["X", "X", "X", "O", "_", "_", "_"],
            ["X", "O", "O", "O", "_", "_", "_"],
        ]
        score = self.ai.evaluate_board(self.game, "X")
        self.assertEqual(score, -1045)

    def test_evaluate_board_case_3(self):
        """
        Test for evaluating the board.
        """
        self.game.board = [
            ["X", "_", "_", "_", "_", "_", "_"],
            ["O", "_", "_", "_", "_", "_", "_"],
            ["X", "O", "_", "_", "_", "_", "O"],
            ["X", "X", "O", "_", "O", "O", "X"],
            ["O", "X", "O", "_", "O", "X", "O"],
            ["O", "O", "X", "X", "X", "X", "X"],
        ]
        score = self.ai.evaluate_board(self.game, "O")
        self.assertEqual(score, 2087)

    def test_evaluate_board_case_4(self):
        """
        Test for evaluating the board.
        """
        self.game.board = [
            ["_", "_", "_", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "_", "_", "_"],
            ["_", "_", "_", "O", "X", "_", "_"],
            ["_", "_", "O", "X", "O", "_", "_"],
            ["_", "_", "O", "O", "X", "_", "X"],
            ["O", "_", "X", "O", "X", "_", "X"],
        ]
        score = self.ai.evaluate_board(self.game, "O")
        self.assertEqual(score, 1055)

    def test_minimax_5_move_win(self):
        """
        Test for minimax decision making win in 5 moves.
        """
        self.game.board = [
            ["O", "O", "O", "X", "_", "O", "_"],
            ["X", "X", "O", "X", "_", "O", "O"],
            ["O", "X", "O", "O", "_", "X", "O"],
            ["X", "O", "X", "X", "_", "O", "X"],
            ["O", "X", "X", "O", "_", "O", "X"],
            ["X", "X", "O", "X", "X", "X", "O"],
        ]
        score, move, tl = self.ai.best_move(self.game)
        self.assertEqual(score, 100000)

    def test_minimax_3_move_win(self):
        """
        Test for minimax decision making win in 3 moves.
        """
        self.game.board = [
            ["O", "X", "O", "X", "_", "O", "X"],
            ["O", "X", "O", "X", "_", "O", "O"],
            ["O", "X", "O", "O", "_", "X", "O"],
            ["X", "O", "X", "X", "_", "O", "X"],
            ["O", "X", "X", "O", "O", "X", "X"],
            ["O", "X", "O", "X", "X", "X", "O"],
        ]
        score, move, tl = self.ai.best_move(self.game)
        self.assertEqual(score, 100000)

    def test_minimax_5_move_win_case_2(self):
        """
        Test for minimax decision making win in 5 moves.
        """
        self.game.board =[
            ["_", "_", "_", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "_", "_", "_"],
            ["_", "_", "O", "O", "_", "_", "_"],
            ["_", "_", "X", "X", "_", "_", "_"],
            ["_", "_", "X", "X", "O", "_", "_"],
            ["O", "O", "X", "X", "X", "O", "O"],
        ]
        score, move, tl = self.ai.best_move(self.game)
        self.assertEqual(score, 100000)

    def test_minimax_3_move_win_case_2(self):
        """
        Test for minimax decision making win in 3 moves.
        """
        self.game.board =[
            ["_", "_", "_", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "_", "_", "_"],
            ["_", "_", "O", "O", "O", "_", "_"],
            ["_", "_", "X", "X", "X", "_", "_"],
            ["_", "_", "X", "X", "O", "_", "_"],
            ["O", "O", "X", "X", "X", "O", "O"],
        ]
        score, move, tl = self.ai.best_move(self.game)
        self.assertEqual(score, 100000)

    def test_best_time_limit_exceed(self):
        """
        Test for best move selection.
        """
        self.game.board = [
            ["_", "_", "_", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "_", "_", "_"],
            ["X", "_", "_", "_", "_", "_", "_"],
            ["O", "O", "_", "_", "X", "O", "O"],
            ["X", "X", "_", "_", "O", "X", "X"],
        ]
        score, move, tl = self.ai.best_move(self.game)
        self.assertTrue(tl)

    def test_ai_chooses_best_heuristic_move_depth_1(self):
        """
        Test for best move selection with depth 1.
        """

        self.ai.depth = 1
        self.game.board =[
            ["_", "_", "_", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "_", "_", "_"],
            ["_", "_", "O", "X", "_", "O", "_"],
            ["_", "_", "X", "X", "O", "O", "O"],
        ]
        score, move, tl = self.ai.best_move(self.game)
        self.assertEqual(score, 1016)
        self.assertEqual(move, 3)

    def test_no_win(self):
        """
        Test for full board detection.
        """

        self.game.board =[
            ["X", "O", "X", "O", "X", "O", "X"],
            ["X", "O", "X", "O", "X", "O", "X"],
            ["O", "X", "O", "X", "O", "X", "O"],
            ["O", "X", "O", "X", "O", "X", "O"],
            ["X", "O", "X", "O", "X", "O", "X"],
            ["X", "O", "X", "O", "X", "O", "X"],
        ]
        score, move, tl = self.ai.best_move(self.game)
        self.assertEqual(score, 0)
        self.assertEqual(move, None)