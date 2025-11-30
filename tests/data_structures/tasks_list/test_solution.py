from contextlib import redirect_stdout
from io import StringIO

from tasks.data_structures.tasks_list.solution import Node, solution


def test_single_node():
    """Тестирует решение с одноэлементным списком."""
    node = Node("single")
    expected = "single\n"

    f = StringIO()
    with redirect_stdout(f):
        solution(node)
    assert f.getvalue() == expected


def test_multiple_nodes():
    """Тестирует решение с многоэлементным списком."""
    node3 = Node("node3")
    node2 = Node("node2", node3)
    node1 = Node("node1", node2)
    node0 = Node("node0", node1)

    expected = "node0\nnode1\nnode2\nnode3\n"

    f = StringIO()
    with redirect_stdout(f):
        solution(node0)
    assert f.getvalue() == expected


def test_different_values():
    """Тестирует решение с узлами, содержащими разные типы данных (int, str, None)."""
    node2 = Node(42)
    node1 = Node("hello", node2)
    node0 = Node(None, node1)

    expected = "None\nhello\n42\n"

    f = StringIO()
    with redirect_stdout(f):
        solution(node0)
    assert f.getvalue() == expected


def test_long_list():
    """Тестирует решение с длинным списком (10 элементов)."""
    head = None
    for i in range(9, -1, -1):
        head = Node(f"item{i}", head)

    expected = "\n".join(f"item{i}" for i in range(10)) + "\n"

    f = StringIO()
    with redirect_stdout(f):
        solution(head)
    assert f.getvalue() == expected


def test_no_mutation():
    """Тестирует, что функция solution не изменяет структуру списка."""
    node2 = Node("b")
    node1 = Node("a", node2)
    original_next = node1.next_item

    f = StringIO()
    with redirect_stdout(f):
        solution(node1)

    assert node1.next_item is original_next
