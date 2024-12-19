from itertools import chain

from dataclasses import dataclass


@dataclass
class BookInfo:
    title: str
    author: str
    isbn_10: str
    isbn_13: str


class ISBN:

    def validate(self, number):
        digits = [int(c) for c in self.sanitize_input(number)]
        if len(digits) != 13:
            return False

        checksum = digits.pop()
        odd_indexes = digits[::2]
        even_indexes = digits[1::2]

        even_indexes_mul_3 = [3*digit for digit in even_indexes]

        digit_sum = sum(chain(odd_indexes, even_indexes_mul_3))
        digit_sum_mod_10 = digit_sum % 10
        digit_sum_mod_10_subtracted_from_10 = 10 - digit_sum_mod_10

        return (digit_sum_mod_10_subtracted_from_10 % 10) == checksum

    def validateISBN10(self, number):
        digits = [c for c in self.sanitize_input(number)]
        if len(digits) != 10:
            return False

        checksum = digits.pop()

        checksum = 10 if checksum == 'X' else int(checksum)
        digits = [int(c) for c in digits]

        # [(1, digits[0]), (2, digits[1]), ...]
        enumerated_digits = enumerate(digits, start=1)
        digit_sum = sum([index * digit for (index, digit) in enumerated_digits])

        return (digit_sum % 11) == checksum

    def sanitize_input(self, value):
        """
        Remove dashes and spaces from input.
        """
        value = value.replace("-", "")
        value = value.replace(" ", "")
        return value
