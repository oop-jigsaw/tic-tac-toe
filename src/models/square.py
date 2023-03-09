class Square:
    def __init__(self, x, y, board, store):
        
        self.board_id = board.id
        self.store = store
        store['squares'].append(self)
        self.id = len(store['squares'])
        self.x = x
        self.y = y

    def turn(self):
        potential_turns = [turn for turn in self.store['turns'] if turn.square_id == self.id]
        if potential_turns:
            return potential_turns[0] 
        
    def board(self):
        return [board for board in self.store['boards'] if board.id == self.board_id][0]
        