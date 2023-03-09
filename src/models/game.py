class Game:
    def __init__(self, user_1, user_2, board, store) -> None:
        self.user_1 = user_1
        self.user_2 = user_2
        self.board_id = board.id
        self.store = store
        store['games'].append(self)

    def board(self):
        return [board for board in self.store['boards'] if board.id == self.board_id][0]
    
    def turns(self, sort = True):
        squares = self.board().squares()
        turns = [square.turn() for square in squares if square.turn()]
        if sort:
            return list(sorted(turns, key = lambda turn: turn.turn_number))
        else:
            return turns
        
        

        