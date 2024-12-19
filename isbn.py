from functools import partial
from itertools import chain
from operator import mul


class ISBN:

    def validate(self, number):
        digits = self.sanitize_input(number)
        if len(digits) != 13:
            return False

        checksum = digits.pop()
        odd_indexes = digits[::2]
        even_indexes = digits[1::2]

        even_indexes_mul_3 = map(partial(mul, 3), even_indexes)

        digit_sum = sum(chain(odd_indexes, even_indexes_mul_3))
        digit_sum_mod_10 = digit_sum % 10
        digit_sum_mod_10_subtracted_from_10 = 10 - digit_sum_mod_10

        return (digit_sum_mod_10_subtracted_from_10 % 10) == checksum

    def sanitize_input(self, value):
        """
        Remove dashes and spaces from input.
        """
        value = value.replace("-", "")
        value = value.replace(" ", "")
        return value
