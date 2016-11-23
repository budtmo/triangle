from unittest import TestCase

from triangle import cli


class TestApp(TestCase):
    """Unit test to test triangle app."""

    def test_equilateral(self):
        output = cli.analyse(3, 3, 3)
        self.assertEqual('equilateral', output.lower())

    def test_isosceles(self):
        output = cli.analyse(3, 3, 1)
        self.assertEqual('isosceles', output.lower())

    def test_scalene(self):
        output = cli.analyse(3, 4, 5)
        self.assertEqual('scalene', output.lower())

    def test_not_triangle(self):
        output = cli.analyse(3, 4, 7)
        self.assertTrue('not' in output.lower())

    def test_unknown_type(self):
        output = cli.analyse(3, 5, 7)
        self.assertTrue('todo' in output.lower())
