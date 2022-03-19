import unittest

from easterformula_module.easterformula import calculateEasterSundayDate


class EasterFormulaTest(unittest.TestCase):
    """simple test that we can calculate the correct Easter Sunday date"""

    def test_calculateEasterSundayDate_for2020_calculatesRightResult(self):
        self.assertEqual("2020-04-12", calculateEasterSundayDate(2020))

    def test_calculateEasterSundayDate_for2021_calculatesRightResult(self):
        self.assertEqual("2021-04-04", calculateEasterSundayDate(2021))

    def test_calculateEasterSundayDate_for2022_calculatesRightResult(self):
        self.assertEqual("2022-04-17", calculateEasterSundayDate(2022))


def main():
    unittest.main()


if __name__ == '__main__':
    main()
