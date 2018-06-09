from unittest import TestCase

from src.Cell import Cell


class TestCell(TestCase):
    def test_should_turn_dead_when_a_live_cell_have_2_alive_neighbour(self):
        # given
        cell = Cell(True)
        number_of_alive_neighbour = 1

        # when
        cell.next(number_of_alive_neighbour)

        # then
        self.assertFalse(cell.state)

    def test_should_turn_dead_when_a_cell_have_more_than_3_alive_neighbour(self):
        # given
        cell = Cell(True)
        number_of_alive_neighbour = 4

        # when
        cell.next(number_of_alive_neighbour)

        # then
        self.assertFalse(cell.state)

    def test_should_turn_alive_when_a_cell_have_3_alive_neighbour(self):
        # given
        cell = Cell(False)
        number_of_alive_neighbour = 3

        # when
        cell.next(number_of_alive_neighbour)

        # then
        self.assertTrue(cell.state)

    def test_should_keep_dead_when_a_dead_cell_have_2_alive_neighbour(self):
        # given
        cell = Cell(False)

        number_of_alive_neighbour = 2

        # when
        cell.next(number_of_alive_neighbour)

        # then
        self.assertFalse(cell.state)

    def test_should_keep_alive_when_a_alive_cell_have_2_alive_neighbour(self):
        # given
        cell = Cell(True)

        number_of_alive_neighbour = 2

        # when
        cell.next(number_of_alive_neighbour)

        # then
        self.assertTrue(cell.state)
