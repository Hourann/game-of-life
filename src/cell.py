class Cell(object):
    def __init__(self, state):
        self.state = state

    def next(self, number_of_alive_neighbour):
        if number_of_alive_neighbour < 2 or number_of_alive_neighbour > 3:
            self.state = False
        elif number_of_alive_neighbour == 3:
            self.state = True

    def __repr__(self):
        return '<Cell: {}>'.format(self.state)

    __str__ = __repr__