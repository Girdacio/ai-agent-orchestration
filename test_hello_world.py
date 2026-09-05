import unittest

from main import Main, FatorRecuperacao


class TestHelloWorld(unittest.TestCase):
    def test_hello_world(self):
        self.assertEqual(Main().hello_world(), "Hello, World!")

    def test_fator_de_recuperacao(self):
        self.assertAlmostEqual(FatorRecuperacao().calcular(0.20), 0.25)
        self.assertAlmostEqual(FatorRecuperacao().calcular(0.10), 0.11)
        self.assertAlmostEqual(FatorRecuperacao().calcular(0.50), 1.0)
        self.assertAlmostEqual(FatorRecuperacao().calcular(0.90), 9.0)


if __name__ == "__main__":
    unittest.main()
