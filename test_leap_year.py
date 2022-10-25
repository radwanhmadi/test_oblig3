from leap_year import isLeapYear


def test_is_divisible_by_4():
    assert isLeapYear(4) == True


def test_is_not_divisible_by_100():
    assert isLeapYear(100) == False


def test_is_divisible_by_400():
    assert isLeapYear(400) == True


def test_is_not_divisible_by_4():
    assert isLeapYear(4) == False


def test_is_divisible_by_100():
    assert isLeapYear(100) == False


def test_is_not_divisible_by_400():
    assert isLeapYear(400) == True