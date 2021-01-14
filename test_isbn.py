# -*- coding: utf-8 -*-
import unittest

from isbn import ISBN


class ISBNTest(unittest.TestCase):
    def test_needs_a_better_name(self):
        # Arrange
        sut = ISBN()
 
        # Act
        result = sut.validate("9780470059029")


        # Assert
        self.assertEqual(True, result)


if __name__ == '__main__':
    unittest.main()