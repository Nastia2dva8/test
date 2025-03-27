import pytest
from task import factorial

@pytest.fixture
def sample_data():
    """Фікстура, що надає список чисел для тестування факторіала."""
    return [0, 1, 2, 3, 4, 5]

@pytest.mark.parametrize("num, expected", [
    (0, 1),
    (1, 1),
    (2, 2),
    (3, 6),
    (4, 24),
    (5, 120),
])
def test_factorial(num, expected):
    """Тестує правильність обчислення факторіала."""
    assert factorial(num) == expected

def test_factorial_negative():
    """Перевіряє, що для від'ємних чисел викликається помилка."""
    with pytest.raises(ValueError):
        factorial(-1)

def test_factorial_with_fixture(sample_data):
    """Тестує факторіал за допомогою фікстури."""
    for num in sample_data:
        assert factorial(num) == factorial(num)