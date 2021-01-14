def sanitize(isbn_number: str):
    return isbn_number.replace(" ", "").replace("-", "")
