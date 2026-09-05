import unittest

from main import Main


class TestHelloWorld(unittest.TestCase):
    def test_hello_world(self):
        self.assertEqual(Main().hello_world(), "Hello, World!")


if __name__ == "__main__":
    unittest.main()
