from tasks.recursion.binary_search.solution import binary_search


def test_empty():
    """Пустой массив."""
    assert binary_search([], 10) == -1


def test_single_element():
    """Массив из одного элемента."""
    assert binary_search([5], 5) == 0
    assert binary_search([5], 6) == -1


def test_duplicates():
    """Поиск среди дубликатов."""
    arr = [1, 2, 2, 4, 7]
    result = binary_search(arr, 2)
    assert result in (1, 2)


def test_negative_numbers():
    """Поиск в массиве с отрицательными числами."""
    arr = [-10, -5, 0, 5, 10]
    assert binary_search(arr, -5) == 1
    assert binary_search(arr, 6) == -1


def test_not_found():
    """Элемент отсутствует в массиве."""
    arr = [1, 3, 5, 7]
    assert binary_search(arr, 4) == -1


def test_large_array():
    """Проверка на большом массиве (логарифмическое поведение)."""
    arr = list(range(1_000_000))
    assert binary_search(arr, 999999) == 999999
    assert binary_search(arr, 1_000_000) == -1
