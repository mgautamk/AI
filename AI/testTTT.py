from ttt import Game
from ttt import availableMoves, isComplete, winner, makeMove, x_won, o_won, tied, determine, equal
import random, unittest

class TestBasicFunctions(unittest.TestCase):
    def setUp(self):
        self.game = Game()

    def test_game_initializes_with_grid(self):
        self.assertEqual(self.game.grid, '         ')

    def test_available_moves(self):
        self.assertEqual(availableMoves(self.game.grid), [0, 1, 2, 3, 4, 5, 6, 7, 8])

    def test_current_turn(self):
        self.assertEqual(self.game._currentTurn, 'x')
        self.game.swapTurn()
        self.assertEqual(self.game._currentTurn, 'o')
        self.game.swapTurn()
        self.assertEqual(self.game._currentTurn, 'x')

    def test_is_game_complete(self):
        self.game.grid = 'xoxoxoxox'
        self.assertEqual(isComplete(self.game.grid), True)
        self.game.grid = '   ooo   '
        self.assertEqual(isComplete(self.game.grid), True)
        self.game.grid = '         '
        self.assertEqual(isComplete(self.game.grid), False)

    def test_equals_method(self):
        self.assertEqual(equal(['x', 'o', 'x']), False)
        self.assertEqual(equal(['x', 'x', 'x']), True)
        self.assertEqual(equal([' ', ' ', 'x']), False)
        self.assertEqual(equal([' ', ' ', ' ']), True)

    def test_winning_board_state(self):
        self.game.grid = 'xxx      '
        self.assertEqual(winner(self.game.grid), 'x')

        self.game.grid = 'xoxoxoxox'
        self.assertEqual(winner(self.game.grid), 'x')

    def test_make_move(self):
        self.game.grid = '         '
        self.assertEqual(makeMove(self.game.grid, 'x', 4), '    x    ')

    def test_erasing_a_move(self):
        self.game.grid = 'x        '
        self.assertEqual(makeMove(self.game.grid, ' ', 0), '         ')

    def test_x_won(self):
        self.game.grid = 'xxx      '
        self.assertEqual(x_won(self.game.grid), True)

    def test_o_won(self):
        self.game.grid = 'ooo      '
        self.assertEqual(o_won(self.game.grid), True)

    def test_tie_game(self):
        self.game.grid = 'xoxoxooxo'
        self.assertEqual(tied(self.game.grid), True)

    def test_game_ends_with_winner(self):
        self.game.grid = 'xxx      '
        self.assertEqual(isComplete(self.game.grid), True)

    def test_swap_move(self):
        self.game._currentTurn = 'x'
        self.game.swapTurn()
        self.assertEqual(self.game._currentTurn, 'o')
        self.game.swapTurn()
        self.assertEqual(self.game._currentTurn, 'x')

class TestSetUpExemptFunctions(unittest.TestCase):
    def test_game_initializes_with_existing_grid(self):
        self.game = Game('xoxoxoxox')
        self.assertEqual(self.game.grid, 'xoxoxoxox')

class TestAIMoves(unittest.TestCase):
    def setUp(self):
        self.game = Game()
        random.seed(14)

    def test_computer_player_makes_winning_move(self):
        self.game.grid = 'oxoxox ox'
        self.assertEqual(makeMove(self.game.grid, 'o', determine(self.game.grid, 'o')), 'oxoxoxoox')

    def test_determine_returns_only_location(self):
        self.game.grid = 'xoxoxoxx '
        self.assertEqual(determine(self.game.grid, 'o'), 8)

    def test_determine_blocks_next_turn_win(self):
        self.game.grid = ' xooxxx o'
        self.assertEqual(determine(self.game.grid, 'o'), 7)

    # broken test, needs a valid board state
    # def test_determine_blocks_another_win(self):
    #     self.game.grid = 'x   x xoo'
    #     self.assertEqual(determine(self.game.grid, 'o'), 2)

    def test_determine_finds_early_win(self):
        self.game.grid = 'o xoxx   '
        self.assertEqual(determine(self.game.grid, 'o'), 6)
