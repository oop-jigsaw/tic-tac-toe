class Turn:
    def __init__(self, square, user, store) -> None:  
        self.square_id = square.id
        self.user_id = user.id
        self.store = store
        store['turns'].append(self)
        
        self.id = len(store['turns'])
        
        turn_number = len(self.game().turns(sort = False))
        self.turn_number = turn_number

    def square(self):
        return [square for square in self.store['squares'] 
         if self.square_id == square.id][0]
    
    def game(self):
        return self.square().board().game()