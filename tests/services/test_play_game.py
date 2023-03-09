from src.services.play_game import PlayGame
from src.models.index import build_store
from src.models.board import Board

def test_build_board_with_squares_builds_nine():
    store =build_store()
    game_play = PlayGame()
    board = Board(store)
    store =build_store()
    squares = game_play.build_squares(board, store)
    assert len(squares) == 9

def test_each_row_has_three_squares():
    store =build_store()
    game_play = PlayGame()
    board = Board(store)
    
    squares = game_play.build_squares(board, store)
    first_square = squares[0]
    assert first_square.x == 1
    assert first_square.y == 1
    second_square = squares[1]
    assert second_square.x == 2
    assert second_square.y == 1

    third_square = squares[2]
    assert third_square.x == 3
    assert third_square.y == 1

    fourth_square = squares[3]
    assert fourth_square.x == 1
    assert fourth_square.y == 2

def test_make_turn():
    store =build_store()
    game_play = PlayGame()
    game = game_play.build_game('sam', 'bob', store)
    game_play.make_turn(game, game.user_1, y_val = 1, x_val = 2, store = store)
    
    first_turn = game.turns()[0]
    assert first_turn.square().x == 2
    assert first_turn.square().y == 1


def test_validate_turn():
    pass
    # turn cannot already be taken
    # turn must be for a square that exists
    # cannot be more moves than are available squares