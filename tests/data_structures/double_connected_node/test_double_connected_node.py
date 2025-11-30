from tasks.data_structures.double_connected_node.solution import DoubleConnectedNode, solution


def test_single_node():
    """Проверка разворота списка с одним узлом."""
    node = DoubleConnectedNode(42)
    new_head = solution(node)
    assert new_head is node
    assert new_head.next is None
    assert new_head.prev is None


def test_two_nodes():
    """Проверка разворота списка с двумя узлами и связей."""
    a = DoubleConnectedNode("first")
    b = DoubleConnectedNode("second")
    a.next = b
    b.prev = a

    new_head = solution(a)
    assert new_head is b
    assert new_head.next is a
    assert new_head.prev is None
    assert a.next is None
    assert a.prev is b


def test_three_nodes():
    """Проверка разворота списка с тремя узлами."""
    n0 = DoubleConnectedNode(1)
    n1 = DoubleConnectedNode(2)
    n2 = DoubleConnectedNode(3)

    n0.next = n1
    n1.prev = n0
    n1.next = n2
    n2.prev = n1

    new_head = solution(n0)
    assert new_head is n2
    assert n2.next is n1
    assert n1.next is n0
    assert n0.next is None
    assert n0.prev is n1
    assert n1.prev is n2
    assert n2.prev is None


def test_example_from_task():
    """Проверка разворота типового списка (4 узла)."""
    node3 = DoubleConnectedNode("node3")
    node2 = DoubleConnectedNode("node2")
    node1 = DoubleConnectedNode("node1")
    node0 = DoubleConnectedNode("node0")

    node0.next = node1
    node1.prev = node0
    node1.next = node2
    node2.prev = node1
    node2.next = node3
    node3.prev = node2

    new_head = solution(node0)
    assert new_head is node3
    assert node3.next is node2
    assert node2.next is node1
    assert node1.next is node0
    assert node0.next is None
    assert node3.prev is None
    assert node2.prev is node3
    assert node1.prev is node2
    assert node0.prev is node1


def test_five_nodes_order():
    """Проверка разворота пяти узлов и порядка значений."""
    values = ["A", "B", "C", "D", "E"]
    nodes = [DoubleConnectedNode(v) for v in values]
    for i in range(4):
        nodes[i].next = nodes[i + 1]
        nodes[i + 1].prev = nodes[i]

    new_head = solution(nodes[0])

    expected = ["E", "D", "C", "B", "A"]
    current = new_head
    for val in expected:
        assert current.value == val
        current = current.next
    assert current is None
    assert new_head.prev is None


def test_large_list_1000_nodes():
    """Проверка разворота большого списка (1000 узлов)."""
    n = 1000
    nodes = [DoubleConnectedNode(i) for i in range(n)]
    for i in range(n - 1):
        nodes[i].next = nodes[i + 1]
        nodes[i + 1].prev = nodes[i]

    new_head = solution(nodes[0])

    assert new_head.value == 999
    assert new_head.prev is None

    current = new_head
    for i in range(999, -1, -1):
        assert current.value == i
        current = current.next
    assert current is None
