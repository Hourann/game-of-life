from unittest import TestCase

from src.table import Table


class TestTable(TestCase):

    def test_if_init_state_is_not_given_then_set_all_cell_to_alive(self):
        # given
        table = Table(3,3,500)

        # then
        for row in table._cells:
            self.assertTrue(all(cell.state for cell in row))

    def test_get_state_method_works_right_in_all_cells_alive_condition(self):
        # given
        table = Table(3, 3)

        # then
        self.assertEqual(table.get_state(), [[True, True, True], [True, True, True], [True, True, True]])