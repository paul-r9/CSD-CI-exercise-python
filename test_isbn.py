from isbn import ISBN, BookInfo

import pytest

test_BookInfoinfo_records = [
    BookInfo(
        "97 Things Every Programmer Should Know",
        "Kevlin Henney",
        "0596809484",
        "9780596809485",
    ),
    BookInfo("Accelerate", "Forsgren, Humble, Kim", "1942788339", "9781942788331"),
    BookInfo(
        "Pattern-Oriented SW Architecture Vol 1",
        "Frank Buschmann",
        "0471958697",
        "9780471958697",
    ),
    BookInfo(
        "Pattern-Oriented SW Architecture Vol 2",
        "Douglas Schmidt",
        "0471606952",
        "9780471606956",
    ),
    BookInfo(
        "Pattern-Oriented SW Architecture Vol 3",
        "Michael Kircher",
        "0478084525",
        "9780470845257",
    ),
    BookInfo(
        "Pattern-Oriented SW Architecture Vol 4",
        "Frank Buschmann",
        "0470059028",
        "9780470059029",
    ),
    BookInfo(
        "Pattern-Oriented SW Architecture Vol 5",
        "Frank Buschmann",
        "0471486485",
        "9780471486480",
    ),
    BookInfo("Refactoring", "Martin Fowler", "0201485672", "9780201485677"),
    BookInfo("Refactoring 2nd Edition", "Martin Fowler", "0134757599", "9780134757599"),
    BookInfo(
        "Test Driven Development by Example", "Kent Beck", "0321146530", "9780321146533"
    ),
    BookInfo("The Laws of Simplicity", "John Maeda", "0262134721", "9780262134729"),
    BookInfo("The Thief Lord", "Cornelia Funke", "043942089X", "9780439420891"),
    BookInfo(
        "Working Effectively with Legacy Code",
        "Michael Feathers",
        "0131177052",
        "9780131177055",
    ),
    BookInfo("xUnit Test Patterns", "Gerard Meszaros", "0131495054", "9780131495050"),
]


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


def test_valid_ISBN10():

    sut = ISBN()

    result = sut.validateISBN10("0201485672")

    assert result


def test_valid_ISBN10_X_at_end():

    sut = ISBN()

    result = sut.validateISBN10("0439-42089-X")

    assert result


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
