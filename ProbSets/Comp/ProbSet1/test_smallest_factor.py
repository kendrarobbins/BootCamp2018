


import pytest
import functions_PS1 as func

#problem 1
def test_small():
    assert func.smallest_factor(1) == 1, "smallest_factor failed for 1"

    assert func.smallest_factor(2) == 2, "smallest_factor failed for 2"

    assert func.smallest_factor(17) == 17, "smallest_factor failed for 17"

    assert func.smallest_factor(25) == 5, "smallest_factor failed for 5"

    assert func.smallest_factor(4) == 2, "smallest_factor failed for 4"

    assert func.smallest_factor(6) == 2, "smallest_factor failed for 6"

    assert func.smallest_factor(8) == 2, "smallest_factor failed for 8"

    assert func.smallest_factor(16) == 2, "smallest_factor failed for 16"
