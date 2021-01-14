from sanitizer import sanitize

class ISBN:

    def validate(self, number):
        return self.checkSum(number)

    def checkSum(self, number):
        isbn_number = number[0:-1]
        checkDigit = int(number[-1])
        sum = 0
        for index, digit in enumerate(isbn_number):
            if index % 2 == 1:
                sum += 3*int(digit)
            else:
                sum += int(digit)
        modulo10_result = sum % 10
        calculated_check_sum_digit = 10 - modulo10_result
        if calculated_check_sum_digit == checkDigit:
            return True
        return False