from unittest import TestCase

from src.table import Table


class TestTable(TestCase):

    def test_if_init_state_is_not_given_then_set_all_cell_to_alive(self):
        # given
        table = Table(3,3,500)

        # then
        for row in table._cells:
            self.assertTrue(all(cell.state for cell in row))

    def test_set_state_method_works_correct_if_given_correct_state(self):
        # given
        table = Table(3,3)
        state = [[True, False, True], [True, False, True], [True, False, True]]

        # when
        table.set_state(state)

        # then
        self.assertEqual(table.get_state(), state)

    def test_get_state_method_works_correct_in_all_cells_alive_condition(self):
        # given
        table = Table(3, 3)

        # then
        self.assertEqual(table.get_state(), [[True, True, True], [True, True, True], [True, True, True]])

    def test_if_size_of_input_state_not_suit_size_of_table_then_raise_exception(self):
        # given
        table = Table(3, 3)
        state = [[True]]

        with self.assertRaises(ValueError):
            table.set_state(state)

    def test_get_num_of_alive_neighbor_works_correct_if_location_is_not_on_the_border(self):
        # given
        table = Table(3,3)
        state = [[True, False, True], [True, False, True], [True, False, True]]
        # when
        table.set_state(state)

        # then
        self.assertEqual(table.num_of_alive_neighbor(1,1), 6)

    def test_get_num_of_alive_neighbor_works_correct_if_location_is_on_the_corner(self):
        # given
        table = Table(3, 3)
        state = [[True, False, True], [True, False, True], [True, False, True]]

        # when
        table.set_state(state)

        # then
        self.assertEqual(table.num_of_alive_neighbor(0, 0), 1)



