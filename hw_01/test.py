import unittest
from tic_tac_game import TicTacGame


class SomeTest(unittest.TestCase):
    def setUp(self):
        self.game = TicTacGame()

    def test_init_board(self):
        self.game.init_board()
        self.assertListEqual(self.game.board, [[' '] * 3 for i in range(3)])
        self.assertEqual(self.game.board_size, 3)

        self.game.init_board(5)
        self.assertListEqual(self.game.board, [[' '] * 5 for i in range(5)])
        self.assertEqual(self.game.board_size, 5)

    def test_init_game(self):
        self.game.init_game()
        self.assertListEqual(self.game.board, [[' '] * 3 for i in range(3)])
        self.assertEqual(self.game.board_size, 3)
        self.assertEqual(self.game.player, self.game.Winner.PLAYER_1)

        self.game.init_game(5)
        self.assertListEqual(self.game.board, [[' '] * 5 for i in range(5)])
        self.assertEqual(self.game.board_size, 5)
        self.assertEqual(self.game.player, self.game.Winner.PLAYER_1)

    def test_switch_player(self):
        self.game.init_game()
        self.assertEqual(self.game.player, self.game.Winner.PLAYER_1)

        self.game.switch_player()
        self.assertEqual(self.game.player, self.game.Winner.PLAYER_2)
        self.game.switch_player()
        self.assertEqual(self.game.player, self.game.Winner.PLAYER_1)

    def test_make_move(self):
        self.game.init_game()

        self.game.make_move(1, 2)
        self.assertEqual(self.game.board[2][1], self.game.Winner.PLAYER_1)

        self.game.make_move(2, 2)
        self.assertEqual(self.game.board[2][2], self.game.Winner.PLAYER_2)

    def test_validate_input(self):
        self.game.init_game()

        self.assertEqual(self.game.validate_input('1 2'), (0, 1))
        self.assertEqual(self.game.validate_input('3 3'), (2, 2))

        self.assertFalse(self.game.validate_input('5 3'))
        self.assertFalse(self.game.validate_input('2'))
        self.assertFalse(self.game.validate_input('2 fdfsd'))
        self.assertFalse(self.game.validate_input('dffsd'))
        self.assertFalse(self.game.validate_input('dfsedg'))

        self.game.make_move(2, 2)
        self.assertFalse(self.game.validate_input('3 3'))

    def test_check_winner(self):
        self.game.init_game()

        self.game.board = [
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' ']
        ]
        self.assertEqual(self.game.check_winner(0, 0), self.game.Winner.NO)
        self.assertEqual(self.game.check_winner(1, 1), self.game.Winner.NO)
        self.assertEqual(self.game.check_winner(2, 2), self.game.Winner.NO)

        self.game.board = [
            [' ', ' ', ' '],
            [' ', 'X', ' '],
            [' ', ' ', ' ']
        ]
        self.assertEqual(self.game.check_winner(1, 1), self.game.Winner.NO)

        self.game.board = [
            [' ', ' ', ' '],
            ['O', 'X', ' '],
            [' ', ' ', ' ']
        ]
        self.assertEqual(self.game.check_winner(0, 1), self.game.Winner.NO)

        self.game.board = [
            ['X', 'O', 'O'],
            [' ', 'X', ' '],
            [' ', ' ', 'X']
        ]
        self.assertEqual(self.game.check_winner(0, 0),
                         self.game.Winner.PLAYER_1)
        self.assertEqual(self.game.check_winner(1, 1),
                         self.game.Winner.PLAYER_1)
        self.assertEqual(self.game.check_winner(2, 2),
                         self.game.Winner.PLAYER_1)

        self.game.board = [
            ['X', 'O', ' '],
            ['X', 'O', ' '],
            ['X', ' ', ' ']
        ]
        self.assertEqual(self.game.check_winner(0, 0),
                         self.game.Winner.PLAYER_1)
        self.assertEqual(self.game.check_winner(0, 1),
                         self.game.Winner.PLAYER_1)
        self.assertEqual(self.game.check_winner(0, 2),
                         self.game.Winner.PLAYER_1)

        self.game.board = [
            ['O', 'O', 'O'],
            ['X', 'X', ' '],
            ['X', ' ', ' ']
        ]
        self.assertEqual(self.game.check_winner(0, 0),
                         self.game.Winner.PLAYER_2)
        self.assertEqual(self.game.check_winner(1, 0),
                         self.game.Winner.PLAYER_2)
        self.assertEqual(self.game.check_winner(2, 0),
                         self.game.Winner.PLAYER_2)

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
