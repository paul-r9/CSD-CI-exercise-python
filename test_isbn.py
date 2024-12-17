from isbn import ISBN


def test_valid_isbn13():
    # Arrange
    sut = ISBN()

    # Act
    result = sut.validate("9780470059029")

    # Assert
    assert result

# Uncomment when implementation is ready:
# def test_invalid_isbn13():
#     # Arrange
#     sut = ISBN()

#     # Act
#     result = sut.validate("9780470059028")

#     # Assert
#     assert not result


def test_sanitize_remove_dashes():
    # Arrange
    sut = ISBN()

    # Act
    result = sut.sanitize_input("978-0-13-595705-9")

    # Assert
    assert result == "9780135957059"
