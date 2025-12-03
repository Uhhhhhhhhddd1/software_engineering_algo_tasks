class DoubleConnectedNode:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev


def solution(node: DoubleConnectedNode) -> DoubleConnectedNode:
    """
    Разворачивает двусвязный список на месте, меняя местами
    указатели 'next' и 'prev' для каждого узла.

    node: Голова двусвязного списка, который нужно развернуть.
    return: Новый головной узел (бывший хвост списка).
    """
    current = node
    previous = None

    while current:
        next_node = current.next

        current.next = previous
        current.prev = next_node

        previous = current
        current = next_node

    return previous
