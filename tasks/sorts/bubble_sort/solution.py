def bubble_sort(arr):
    """
    Сортирует массив пузырьком по возрастанию.
    Выводит состояние массива после каждого прохода, в котором были обмены.
    Если массив уже отсортирован — выводит его один раз.
    """
    n = len(arr)
    result_states = []

    for i in range(n):
        swapped = False

        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if swapped:
            result_states.append(arr[:])
        if not swapped:
            break
    if not result_states:
        result_states.append(arr[:])

    return result_states
