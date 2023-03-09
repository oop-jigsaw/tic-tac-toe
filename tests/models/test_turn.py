from src.services.play_game import PlayGame
from src.models.index import build_store


def test_make_turn():
    store =build_store()
    game_play = PlayGame()
    game = game_play.build_game('sam', 'bob', store)
    game_play.make_turn(game, game.user_1, y_val = 1, x_val = 2, store = store)
    
    first_turn = game.turns()[0]
    assert first_turn.turn_number == 1
    game_play.make_turn(game, game.user_1, y_val = 1, x_val = 1, store = store)
    second_turn = game.turns()[1]
    # turn_numbers = [turn.turn_number for turn in game.turns()]
    assert second_turn.turn_number == 2
