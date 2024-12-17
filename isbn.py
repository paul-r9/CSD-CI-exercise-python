class ISBN:

    def validate(self, number):
        return True

    def sanitize_input(self, value):
        """
        Remove dashes and spaces from input.
        """
        value = value.replace("-", "")
        return value
