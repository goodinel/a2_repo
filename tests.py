import unittest
from check_pwd import check_pwd
from unittest import TestCase


class Test(TestCase):

    def test1(self):
        self.assertFalse(check_pwd())

    def test2(self):
        self.assertFalse("")


if __name__ == "__main__":
    unittest.main()
