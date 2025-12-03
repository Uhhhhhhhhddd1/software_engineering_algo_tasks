def binary_search(arr: list[int], target: int) -> int:
    """Вернуть индекс target в отсортированном списке arr или -1, если нет."""
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        val = arr[mid]

        if val == target:
            return mid
        if val < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1
