import pytest
import functions_PS1 as func



def test_backpack():
    testpack = func.Backpack("Barry", "black")
    if testpack.name != "Barry":
        print("Backpack.name assigned incorrectly.")

    for item in ["pencil", "pen", "paper", "computer"]:
        testpack.put(item)

    print("contents:", testpack.contents)

test_backpack()
