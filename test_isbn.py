# -*- coding: utf-8 -*-
import unittest

from isbn import ISBN


class ISBNTest(unittest.TestCase):
    def test_valid_isbn13(self):
        # Arrange
        sut = ISBN()
 
        # Act
        result = sut.validate("9780470059029")


        # Assert
        self.assertEqual(True, result)

    def test_invalid_isbn13(self):
        # Arrange
        sut = ISBN()
 
        # Act
        result = sut.validate("9780470059028")


        # Assert
        self.assertEqual(False, result)

if __name__ == '__main__':
    unittest.main()