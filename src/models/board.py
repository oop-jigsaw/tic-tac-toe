import itertools
class Board:
    def __init__(self, store):
        self.store = store
        self.id = len(store['boards']) + 1
        store['boards'].append(self)

    def squares(self):
        return [square for square in self.store['squares']
                 if square.board_id == self.id]

    def rows(self):
        sorted_squares = list(sorted(self.squares(), key = lambda square: square.y))
        grouped = [list(g) for k, g in itertools.groupby(sorted_squares, lambda square: square.y)]
        return grouped
    
    def columns(self):
        sorted_squares = sorted(self.squares(), key = lambda square: square.x)
        grouped = [list(g) for k, g in itertools.groupby(sorted_squares, lambda square: square.x)]
        return grouped
    
    def find_square(self, y_val, x_val):
        return self.rows()[y_val - 1][x_val - 1]
    
    def game(self):
        return [game for game in self.store['games']
                 if game.board_id == self.id][0]

