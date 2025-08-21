# 5.3.1. Файл с функциями
# 5.3.2. Основной файл main
# 5.3.3. Метод grid 
# 5.3.4. Создаем интерфейс
# 5.3.5. Отладка программы
# 5.3.6. Unit-тесты
# 5.3.7. Тестирование с модулем pytest

import calculator_logic as c
import pytest

# Переделываем функцию деления чтобы она выдавала исключения
def divide(a, b):
    if b == 0:
        raise ValueError("Division by zero")
    return a / b

def test_add():
    assert c.add(10, 5) == 15
    assert c.add(-1, 1) == 0
    assert c.add(-2, -2) == -4

    with pytest.raises(TypeError):
        c.add("text", 1)
    with pytest.raises(TypeError):
        c.add(1, "text")

def test_subtract(): 
    assert c.subtract(10, 5) == 5
    assert c.subtract(-1, 1) == -2
    assert c.subtract(-10, -10) == 0

    with pytest.raises(TypeError):
        c.subtract("text", 1)
    with pytest.raises(TypeError):
        c.subtract(1, "text")


def test_multiply():
    assert c.multiply(2, 2) == 4
    assert c.multiply(-5, 6) == -30
    assert c.multiply(-1, -5) == 5

    with pytest.raises(TypeError):
        c.multiply("text", 1)
    with pytest.raises(TypeError):
        c.multiply(1, "text")


def test_divide():
    assert c.divide(10, 2) == 5
    assert c.divide(-10, 2) == -5
    assert c.divide(10, -2) == -5

    with pytest.raises(TypeError):
        c.divide("text", 1)
    with pytest.raises(TypeError):
        c.divide(1, "text")
    with pytest.raises(ZeroDivisionError):
        c.divide(10, 0)

test_add()
test_subtract()
test_multiply()
test_divide()
print("Все тесты пройдены успешно!")
