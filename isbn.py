from sanitizer import sanitize

class ISBN:
    is_isbn_ten = False

    def validate(self, number):
        return self.checkSum(number)

    def checkSum(self, number):
        checkDigit = int(number[-1])
        if not (checkDigit % 2):
            return False
        return True

    def determine_isbn_type(self, isbn_number: str) -> None:
        self.is_isbn_ten = True
