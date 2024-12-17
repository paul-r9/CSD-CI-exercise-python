from isbn import ISBN

import pytest


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
    result = sut.validate("978-0-13-595705-8")

    # Assert
    assert not result


@pytest.mark.parametrize(
    "value,expected",
    [
        ("978-0-13-595705-9", "9780135957059"),
        ("978 0 131 49505 0", "9780131495050"),
        ("978 0 13-595705-9", "9780135957059"),
    ],
)
def test_sanitize_input_dashes_and_spaces(value, expected):
    # Arrange
    sut = ISBN()

    # Act
    result = sut.sanitize_input(value)

    # Assert
    assert result == expected


def test_invalid_isbn13_is_too_short():

    sut = ISBN()

    result = sut.validate("982")

    assert not result


def test_invalid_isbn13_is_too_long():

    sut = ISBN()

    result = sut.validate("97804700590294")

    assert not result


@pytest.mark.parametrize(
    "value",
    [
        "abc-0-13-595705-9",
        "978 ; === 49505 0",
        "978 0 🙄3-595705-9",
    ],
)
def test_invalid_isbn13_bad_inputs(value):

    sut = ISBN()

    try:
        sut.validate(value)
    except ValueError:
        # value errors get raised with garbage inputs
        pass
    else:
        assert False, "did not raise expected ValueError exception"
