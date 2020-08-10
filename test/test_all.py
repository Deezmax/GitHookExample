"""Testing"""
import unittest
from src import check_branch


class MyTestCase(unittest.TestCase):
    """Class for test cases"""

    def test_checkbranch(self):
        """Tests the check_branch module"""
        self.assertEqual(check_branch.main(""), 1)

    def test_checkregex(self):
        """Tests the check_regex module"""

    def test_checkfile(self):
        """Tests the check_file module"""

    def test_lint(self):
        """Tests the lint module"""


if __name__ == '__main__':
    unittest.main()
