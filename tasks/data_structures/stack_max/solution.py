from typing import Optional, Union


class StackMax:
    """
    Стек с O(1) операцией get_max().

    Хранит текущий максимум в отдельном стеке.
    При одинаковых максимумах — дублирует их в max_stack.
    """

    def __init__(self) -> None:
        self._items = []
        self._max_stack = []

    def push(self, x: int) -> None:
        """Добавляет элемент x в стек и обновляет максимум."""
        self._items.append(x)
        if not self._max_stack or x >= self._max_stack[-1]:
            self._max_stack.append(x)

    def pop(self) -> Optional[str]:
        """Удаляет элемент с вершины. Возвращает error, если стек пуст."""
        if not self._items:
            return "error"
        removed = self._items.pop()
        if self._max_stack and removed == self._max_stack[-1]:
            self._max_stack.pop()
        return None

    def get_max(self) -> Union[int, str, None]:
        """Возвращает текущий максимум или 'None' при пустом стеке."""
        return "None" if not self._max_stack else self._max_stack[-1]
