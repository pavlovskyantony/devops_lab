import unittest
from unittest import TestCase

import homework5_2

class Testtask2(TestCase):
    def setUp(self):

        """Init test of Homework2: task2"""


    def test_task2_1(self):
        self.assertEqual(homework5_2.func_task2(2, -6, 6, -2), [1])


    def test_task2_2(self):
        self.assertNotEqual(homework5_2.func_task2(), [1])


    def tearDown(self):

        """Init test is finished"""


if __name__ == '__main__':
    unittest.main()
