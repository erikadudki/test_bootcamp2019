# -*- coding: utf-8 -*-

"""This file contains the tests."""

from unittest import TestCase

from test_bootcamp2019 import add


class TestAdd(TestCase):
    """This test makes sure that addition to zero doesnt do anyting."""

    def test_identity(self):
        """This test makes sure that addition to zero doesnt do anyting."""
        a = 1
        actual = add(a, 0)
        self.assertEqual(a, actual)

    def test_add_negation(self):
        """This test makes sure that addition to zero doesnt do anyting."""
        a = 1
        actual = add(a, -a)
        self.assertEqual(0, actual)

    pass
