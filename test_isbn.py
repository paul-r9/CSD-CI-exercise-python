from isbn import ISBN

def test_valid_isbn13():
    # Arrange
    sut = ISBN()

    # Act
    result = sut.validate("9780131495050")

    # Assert
    assert result