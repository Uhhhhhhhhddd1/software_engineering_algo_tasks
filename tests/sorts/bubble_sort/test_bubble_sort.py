from tasks.sorts.bubble_sort.solution import bubble_sort


def test_already_sorted():
    """Массив уже отсортирован — выводим один раз."""
    arr = [1, 2, 3, 4, 5]
    assert bubble_sort(arr.copy()) == [[1, 2, 3, 4, 5]]


def test_reverse_order():
    """Полностью перевёрнутый массив."""
    arr = [5, 4, 3, 2, 1]
    expected = [[4, 3, 2, 1, 5], [3, 2, 1, 4, 5], [2, 1, 3, 4, 5], [1, 2, 3, 4, 5]]
    assert bubble_sort(arr.copy()) == expected


def test_with_duplicates():
    """Массив с повторяющимися элементами."""
    arr = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    result = bubble_sort(arr.copy())
    assert result[-1] == [1, 1, 2, 3, 4, 5, 5, 6, 9]
    assert len(result) > 1


def test_negative_and_zero():
    """Отрицательные числа и ноль."""
    arr = [0, -5, 10, -3, 7, -8]
    result = bubble_sort(arr.copy())
    assert result[-1] == [-8, -5, -3, 0, 7, 10]
    assert len(result) > 1


def test_example_from_task():
    """Точный пример из условия задачи."""
    arr = [3, 7, 9, 4, 3, 1, 8, 5]
    expected = [
        [3, 7, 4, 3, 1, 8, 5, 9],
        [3, 4, 3, 1, 7, 5, 8, 9],
        [3, 3, 1, 4, 5, 7, 8, 9],
        [3, 1, 3, 4, 5, 7, 8, 9],
        [1, 3, 3, 4, 5, 7, 8, 9],
    ]
    assert bubble_sort(arr.copy()) == expected


def test_two_elements():
    """Минимальный случай — два элемента."""
    assert bubble_sort([2, 1].copy()) == [[1, 2]]
    assert bubble_sort([1, 2].copy()) == [[1, 2]]


def test_large_reverse_sorted():
    """Проверка на максимальном массиве в обратном порядке (n=1000)."""
    arr = list(range(999, -1, -1))  # [999, 998, ..., 1, 0]
    states = bubble_sort(arr.copy())
    assert states[-1] == list(range(1000))

    assert len(states) == 999

    assert states[0][-1] == 999
    assert states[0][0] == 998

    assert states[-1][0] == 0
    assert states[-1][999] == 999
