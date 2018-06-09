class Cell(object):
    def __init__(self, state):
        self.state = state

    def next(self, number_of_alive_neigbour):
        if number_of_alive_neigbour < 2:
            self.state = False