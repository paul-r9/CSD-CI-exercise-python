from sanitizer import sanitize

class ISBN:

    def validate(self, number):
        return self.checkSum(number)

    def checkSum(self, number):
        checkDigit = int(number[-1])
        if not (checkDigit % 2):
            return False
        return True
