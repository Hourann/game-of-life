from unittest import TestCase

from src.table import Table


class TestTable(TestCase):

    def test_if_init_state_is_not_given_then_set_all_cell_to_alive(self):
        # given
        table = Table(3,3)

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

    def test_get_num_of_alive_neighbor_works_correct_if_location_is_on_the_border(self):
        # given
        table = Table(3, 3)
        state = [[True, False, True], [True, False, True], [True, False, True]]

        # when
        table.set_state(state)

        # then
        self.assertEqual(table.num_of_alive_neighbor(0, 1), 2)


    def test_table_next_state_correct_in_case_1(self):
        # given
        # X O X     X X X
        # X O X =>  O O O
        # X O X     X X X
        table = Table(3,3)
        state = [[False, True, False],[False, True, False],[False, True, False]]
        table.set_state(state)
        # when
        table.next()

        # then
        self.assertEqual(table.get_state(), [[False, False, False], [True, True, True], [False, False, False]])

    def test_table_next_state_correct_in_case_2(self):
        # given
        # X X X X     X X X X
        # X O O X =>  X O O X
        # X O O X     X O O X
        # X X X X     X X X X
        table = Table(4, 4)
        state = [[False, False, False, False],[False, True, True, False],[False, True, True, False],[False, False, False, False]]
        table.set_state(state)
        # when
        table.next()

        # then
        self.assertEqual(table.get_state(), state)