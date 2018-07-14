# _*_ coding: utf-8 _*_

__author__ = 'Morgan'

'''
python password test
'''

import unittest
import Mstrange


class TestCheck(unittest.TestCase):

    def test_regular(self):
        rv = Mstrange.password('qwertyuiop')
        self.assertTrue(repr(rv) == "simple")
        self.assertTrue("规则" in rv.message)

    def test_by_step(self):
        rv = Mstrange.password('abcdefgh')
        self.assertTrue(repr(rv) == "simple")
        self.assertTrue("规则" in rv.message)

    def test_strong(self):
        rv = Mstrange.password('12acPA12ACpp')
        self.assertTrue(repr(rv) == "strong")
        self.assertTrue("强度" in rv.message)

if __name__ == '__main__':
    unittest.main()