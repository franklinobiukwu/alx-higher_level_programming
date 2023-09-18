#!/usr/bin/python3
import unittest
from models.base import Base

"""unit test for base class"""


class TestBase(unittest.TestCase):
    """unittest class to test Base class"""

    def test_id_none(self):
        """test base without id (i.e. id=None)"""
        a = Base()
        self.assertEqual(a.id, 1)

    def test_id_pint(self):
        """test base with +ve id"""
        a = Base(20)
        self.assertEqual(a.id, 20)

    def test_id_nint(self):
        """test base with -ve id"""
        a = Base(-20)
        self.assertEqual(a.id, -20)

    def test_id_zero(self):
        """test base with zero id"""
        a = Base(0)
        self.assertEqual(a.id, 0)

    def test_id_str(self):
        """test base with string id"""
        a = Base("a")
        self.assertEqual(a.id, "a")

    def test_id_tup(self):
        """test base with tuple id"""
        a = Base((1, 2))
        self.assertEqual(a.id, (1, 2))

    def test_id_list(self):
        """test base with list id"""
        a = Base([1, 2])
        self.assertEqual(a.id, [1, 2])

    def test_id_dict(self):
        """test base with dictionary id"""
        a = Base({"name": "Frank", "age": 600})
        self.assertEqual(a.id, {"name": "Frank", "age": 600})
