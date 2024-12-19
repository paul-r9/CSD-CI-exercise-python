from isbn import ISBN


def test_valid_isbn13():
    # Arrange
    sut = ISBN()

    # Act
    result = sut.validate("9780470059029")

    # Assert
    assert result


def test_invalid_isbn13_checksum_wrong():
    # Arrange
    sut = ISBN()

    # Act
    result = sut.validate("9780470059028")

    # Assert
    assert not result


def test_invalid_isbn13_is_too_short():

    sut = ISBN()

    result = sut.validate("982")

    assert not result
