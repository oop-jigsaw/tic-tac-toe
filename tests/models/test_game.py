from src.models.index import build_store
from src.models.board import Board
from src.models.user import User
from src.models.game import Game

def test_game_has_two_users_and_a_board():
    store = build_store()
    board = Board(store)
    bob = User(name = 'bob', store = store)
    sam = User(name = 'sam', store = store)
    game = Game(bob, sam, board, store)

def test_game_is_added_to_the_store():
    store = build_store()
    board = Board(store)
    bob = User(name = 'bob', store = store)
    sam = User(name = 'sam', store = store)
    game = Game(bob, sam, board, store)
    assert len(store['games']) == 1

from src.services.play_game import PlayGame
from src.models.index import build_store


def test_turns_returns_turns_in_the_correct_order():
    store =build_store()
    game_play = PlayGame()
    game = game_play.build_game('sam', 'bob', store)
    game_play.make_turn(game, game.user_1, y_val = 1, x_val = 2, store = store)
    
    first_turn = game.turns()[0]
    assert first_turn.turn_number == 1
    game_play.make_turn(game, game.user_1, y_val = 2, x_val = 1, store = store)
    second_turn = game.turns()[1]
    assert second_turn.turn_number == 2
    
