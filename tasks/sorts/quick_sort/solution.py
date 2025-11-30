def quick_sort(arr: list[int]) -> list[int]:
    """Вернуть новый список, отсортированный быстрой сортировкой по возрастанию."""
    if len(arr) <= 1:
        return arr[:]

    pivot = arr[len(arr) // 2]

    left = []
    middle = []
    right = []

    for x in arr:
        if x < pivot:
            left.append(x)
        elif x == pivot:
            middle.append(x)
        else:
            right.append(x)

    return quick_sort(left) + middle + quick_sort(right)
