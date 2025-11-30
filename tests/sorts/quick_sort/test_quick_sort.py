from tasks.sorts.quick_sort.solution import quick_sort


def test_empty():
    """Пустой список должен возвращать пустой."""
    assert quick_sort([]) == []


def test_single():
    """Список из одного элемента должен возвращаться как есть."""
    assert quick_sort([3]) == [3]


def test_example():
    """Проверка примера из условия."""
    assert quick_sort([3, 7, 9, 4, 3, 1, 8, 5]) == [1, 3, 3, 4, 5, 7, 8, 9]


def test_reverse():
    """Корректная сортировка обратного массива."""
    assert quick_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]


def test_duplicates():
    """Корректная сортировка дубликатов и отрицательных чисел."""
    assert quick_sort([2, -1, 2, -1, 0]) == [-1, -1, 0, 2, 2]


def test_large_random():
    """Проверка на массиве длиной 10000 (алгоритмическая сложность)."""
    import random

    arr = [random.randint(-(10**9), 10**9) for i in range(10000)]
    assert quick_sort(arr) == sorted(arr)


def test_already_sorted():
    """Сортировка уже отсортированного массива."""
    arr = list(range(2000))
    assert quick_sort(arr) == arr
