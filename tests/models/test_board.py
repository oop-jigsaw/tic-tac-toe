from src.models.index import build_store
from src.models.board import Board
from src.services.play_game import PlayGame

def test_board_is_added_to_the_store():
    store = build_store()
    board = Board(store)
    assert len(store['boards']) == 1

def test_board_has_three_rows():
    store =build_store()
    game_play = PlayGame()
    board = game_play.build_board_with_squares(store)
    assert len(board.rows()) == 3

def test_y_values_of_row_are_the_same():
    store =build_store()
    game_play = PlayGame()
    board = game_play.build_board_with_squares(store)
    rows = board.rows()
    row_values = [list(set([square.y for square in row])) for row in rows]
    assert row_values == [[1], [2], [3]]

def test_find_square():
    store =build_store()
    game_play = PlayGame()
    board = game_play.build_board_with_squares(store)
    square = board.find_square(1, 2)
    assert square.y == 1
    assert square.x == 2
    