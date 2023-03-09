from src.models.square import Square
from src.models.board import Board
from src.models.user import User
from src.models.game import Game
from src.models.turn import Turn

class PlayGame:
    def build_game(self, name_1, name_2, store):
        user_1 = User(name = name_1, store = store)
        user_2 = User(name = name_2, store = store)
        board = self.build_board_with_squares(store)
        game = Game(user_1, user_2, board, store)
        return game

    def build_squares(self, board, store, rows = 3, columns = 3):
        squares = []
        for y in range(rows):
            for x in range(columns):
                squares.append(Square(x + 1, y + 1, board, store))
        return squares
    
    def build_board_with_squares(self, store):
        board = Board(store)
        squares = self.build_squares(board, store)
        return board

    def make_turn(self, game, user, y_val, x_val, store):
        board = game.board()
        square = board.find_square(y_val, x_val)
        turn = Turn(square, user, store)
        return turn

        
        