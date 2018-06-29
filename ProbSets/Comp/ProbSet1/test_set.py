import pytest
import functions_PS1 as func



@pytest.fixture
def set_up_hands():
    hand1 = ["1022", "1122", "0100", "2021", "0010", "2201",
             "2111", "0020", "1102", "0210", "2110", "1020"]
    Not12 = ["0000"]
    NotUnique = ["0000", "0000", "0000", "0000", "0000", "0000",
                     "0000", "0000", "0000", "0000", "0000", "0000"]
    WrongDigits = ["00000", "1122", "0100", "2021", "0010", "2201",
                       "2111", "0020", "1102", "0210", "2110", "1020"]
    NotMod3 = ["3022", "1122", "0100", "2021", "0010", "2201",
                     "2111", "0020", "1102", "0210", "2110", "1020"]
    return hand1, not12, NotUnique, WrongDigits, NotMod3


def test_count_sets():

    hand1, not12, NotUnique, WrongDigits, NotMod3 = set_up_hands
    assert func.count_sets(hand1) = 6
    pytest.raises(ValueError, func.count_sets, cards = Not12)
    pytest.raises(ValueError, func.count_sets, cards = NotMod3)
    pytest.raises(ValueError, func.count_sets, cards = NotUnique)
    pytest.raises(ValueError, func.count_sets, cards = WrongDigits)

def test_is_set():

    assert is_set("1010", "0101", "2222") = True
    assert is_set("1111", "0000", "1111") = False
    assert is_set("1000", "1121", "1212") = True
