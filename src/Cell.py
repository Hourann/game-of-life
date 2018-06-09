class Cell(object):
    def __init__(self, state):
        self.state = state

    def next(self, number_of_alive_neighbour):
        if number_of_alive_neighbour < 2:
            self.state = False
        elif number_of_alive_neighbour > 3:
            self.state = False
        elif number_of_alive_neighbour == 3:
            self.state = True
        elif number_of_alive_neighbour == 2:
            pass