from unittest import TestCase

from src.Cell import Cell


class TestCell(TestCase):
    def test_should_turn_dead_when_a_live_cell_have_less_than_2_alive_neigbhour(self):
        # given
        cell = Cell(True)
        number_of_alive_neigbour = 1

        # whenR
        cell.next(number_of_alive_neigbour)

        # then
        self.assertFalse(cell.state)
