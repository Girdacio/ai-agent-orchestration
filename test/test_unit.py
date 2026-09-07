import unittest


def somar(a, b):
    return a + b


class TestSomar(unittest.TestCase):
    def test_somar_numeros_positivos(self):
        self.assertEqual(somar(2, 3), 5)

    def test_somar_zero(self):
        self.assertEqual(somar(0, 5), 5)


if __name__ == "__main__":
    unittest.main()
