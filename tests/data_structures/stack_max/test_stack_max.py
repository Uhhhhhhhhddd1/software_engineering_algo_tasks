from tasks.data_structures.stack_max.solution import StackMax


def test_empty_stack():
    """Тестирует поведение стека при его инициализации (пустой стек)."""
    stack = StackMax()
    assert stack.get_max() == "None"
    assert stack.pop() == "error"


def test_push_get_max():
    """Тестирует операции push и get_max при добавлении элементов."""
    stack = StackMax()
    stack.push(5)
    assert stack.get_max() == 5

    stack.push(1)
    stack.push(10)
    assert stack.get_max() == 10


def test_pop_updates_max():
    """Тестирует, что get_max корректно обновляется после операции pop."""
    stack = StackMax()
    stack.push(1)
    stack.push(3)
    stack.push(2)

    assert stack.pop() is None
    assert stack.get_max() == 3

    assert stack.pop() is None
    assert stack.get_max() == 1

    assert stack.pop() is None
    assert stack.get_max() == "None"


def test_negative_numbers():
    """Тестирует работу стека с отрицательными числами и нулем."""
    stack = StackMax()
    stack.push(-5)
    stack.push(-10)
    assert stack.get_max() == -5

    stack.push(0)
    assert stack.get_max() == 0


def test_example_scenario():
    """Тестирует последовательность операций, имитирующих реальный сценарий использования."""
    stack = StackMax()
    assert stack.get_max() == "None"
    assert stack.pop() == "error"

    stack.push(7)
    assert stack.get_max() == 7

    stack.pop()
    assert stack.get_max() == "None"

    stack.push(-2)
    stack.push(-1)
    assert stack.pop() is None
    assert stack.get_max() == -2
    assert stack.get_max() == -2


def test_multiple_operations():
    """Тестирует стек после большого количества операций push и pop."""
    stack = StackMax()
    items = [3, 1, 4, 1, 5, 9, 2, 6]
    for x in items:
        stack.push(x)
    assert stack.get_max() == 9

    for _ in range(4):
        stack.pop()
    assert stack.get_max() == 4


def test_duplicate_max():
    """Тестирует корректную обработку повторяющихся максимальных элементов."""
    stack = StackMax()
    stack.push(5)
    assert stack.get_max() == 5

    stack.push(5)
    assert stack.get_max() == 5

    stack.push(3)
    assert stack.get_max() == 5

    stack.pop()
    assert stack.get_max() == 5

    stack.pop()
    assert stack.get_max() == 5

    stack.pop()
    assert stack.get_max() == "None"


def test_large_duplicates():
    """Тестирует обработку большого количества дублирующихся максимальных элементов."""
    stack = StackMax()
    stack.push(100000)
    assert stack.get_max() == 100000
    stack.push(100000)
    assert stack.get_max() == 100000
    stack.pop()
    assert stack.get_max() == 100000
    stack.pop()
    assert stack.get_max() == "None"
