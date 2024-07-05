import pytest
from src.decorators import log


@log()
def function_success(x, y):
    return x + y


@log()
def function_fail(x, y):
    raise ValueError("Ошибка!")


def test_function_success(capsys):
    function_success(1, 2)
    captured = capsys.readouterr()
    assert "function_success ok\n" in captured.out


def test_function_fail(capsys):
    with pytest.raises(ValueError):
        function_fail(1, 2)
    captured = capsys.readouterr()
    assert "function_fail error: ValueError. Inputs: (1, 2), {}\n" in captured.out