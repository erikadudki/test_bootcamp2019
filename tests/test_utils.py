from unittest import TestCase
from test_bootcamp2019 import add

class TestAdd(TestCase):

    def test_identity(self):
        """This test makes sure that addition to zero doesnt do anyting."""
        a = 1
        actual = add(a,0)
        self.assertEqual(a,actual)

    def test_add_negation(self):
        a = 1
        expected = 0
        actual = add(a,-a)
        self.assertEqual(0,actual)

    pass