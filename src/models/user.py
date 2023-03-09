class User:
    def __init__(self, name, store):
        self.name = name
        store['users'].append(self)
        self.id = len(store['users'])