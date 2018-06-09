import unittest
from src.run import answer

class TestMain(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(answer(), 42)


if __name__ == '__main__':
    unittest.main()
