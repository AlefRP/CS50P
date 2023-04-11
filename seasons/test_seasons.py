import pytest
from datetime import date, timedelta
import inflect
from seasons import Person, calculate_age_in_minutes, number_to_words, date_is_valid

def test_person_age():
    dob = date.today() - timedelta(days=365)
    person = Person(dob)
    expected_minutes = 365 * 24 * 60
    assert person.age_in_minutes() == expected_minutes
    p = inflect.engine()
    assert person.age_in_words() == p.number_to_words(expected_minutes).capitalize().replace(" and ", " ")

@pytest.mark.parametrize("date_str, expected_result", [
    ("2021-09-15", (True, date(2021, 9, 15))),
    ("2021-04-30", (True, date(2021, 4, 30))),
    ("2021-13-01", (False, None)),
    ("2021-04-31", (False, None)),
    ("invalid_date", (False, None)),
])
def test_date_is_valid(date_str, expected_result):
    assert date_is_valid(date_str) == expected_result

def test_calculate_age_in_minutes():
    dob = date.today() - timedelta(days=365)
    expected_minutes = 365 * 24 * 60
    assert calculate_age_in_minutes(dob) == expected_minutes

def test_number_to_words():
    number = 12345
    p = inflect.engine()
    expected_words = p.number_to_words(number).capitalize().replace(" and ", " ")
    assert number_to_words(number) == expected_words
