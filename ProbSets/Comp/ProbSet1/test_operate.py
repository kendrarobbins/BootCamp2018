import pytest
import functions_PS1 as func


def test_operate():

    assert func.operate(1,2,'+') == 3, "operate fails for addition"
    assert func.operate(1,2,'-') == -1, "operate fails for subtraction"
    assert func.operate(1,2,'*') == 2, "operate fails for multiplication"
    assert func.operate(2,1,'/') == 2, "operate fails for division"
    pytest.raises(ZeroDivisionError, func.operate, a=4, b=0, oper='/')
    pytest.raises(ValueError, func.operate, a=1, b=1, oper='x')
