
import pytest
import functions_PS1 as func

def test_month():

    assert func.month_length("September") == 30, "month_length failed for September"
    assert func.month_length("March") == 31, "month_length failed for March"
    assert func.month_length("February", leap_year=False) == 28, "month_length failed for February, not leap year"
    assert func.month_length("February", leap_year=True) == 29, "month_length failed for February, leap year"
