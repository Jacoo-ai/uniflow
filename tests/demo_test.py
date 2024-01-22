from typing import Sequence
from uniflow.node import Node
from uniflow.op.basic.expand_op import ExpandOp
from uniflow.op.basic.reduce_op import ReduceOp


class DemoTest:
    """Demo Test Class."""

    def __init__(self) -> None:
        self._expand_op = ExpandOp("expand_op")
        self._reduce_op = ReduceOp("reduce_op")

    def expand_test(self, nodes: Sequence[Node]) -> Sequence[Node]:
        """Expand Test.

        Args:
            nodes (Sequence[Node]): Nodes.

        Returns:
            Sequence[Node]: Nodes.
        """
        expanded = self._expand_op(nodes[0], self._expand_op.divide_half)
        return expanded

    def reduce_test(self, nodes: Sequence[Node]) -> Sequence[Node]:
        """Reduce Test.

        Args:
            nodes (Sequence[Node]): Nodes.

        Returns:
            Sequence[Node]: Nodes.
        """
        reduced = self._reduce_op(nodes, self._reduce_op.reduce)
        return reduced

    def expand_reduce_test(self, nodes: Sequence[Node]) -> Sequence[Node]:
        """Expand and Reduce Test.

        Args:
            nodes (Sequence[Node]): Nodes.

        Returns:
            Sequence[Node]: Nodes.
        """
        expanded = self._expand_op(nodes[0], self._expand_op.divide_half)
        reduced = self._reduce_op(expanded, self._reduce_op.reduce)
        return [reduced]


if __name__ == "__main__":
    test = DemoTest()
    input_dict = [{"1": "2", "3": "4", "5": "6", "7": "8"}]
    input_node = [Node(name="input", value_dict=input_dict)]

    '''Expand test'''
    print("root dict:")
    print(input_dict)
    print("expanded dicts:")
    print(test.expand_test(input_node)[0].value_dict)
    print(test.expand_test(input_node)[1].value_dict)
