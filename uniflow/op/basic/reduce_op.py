from typing import Any, Mapping, Sequence
from uniflow.node import Node
from uniflow.op.op import Op


class ReduceOp(Op):
    """Reduce operation class"""

    def __init__(self, name: str) -> None:
        super().__init__(name)

    def transform_reduce(self, value_dicts: Sequence[Mapping[str, Any]]) -> Mapping[str, Any]:
        """Transform value dict.

        Args:
            value_dicts (Sequence[Mapping[str, Any]]): Input 2 dicts.

        Returns:
            Mapping[str, Any]: Output the dict of the reduced node.
        """

        expand_1 = value_dicts[0]
        expand_2 = value_dicts[1]

        out_dict = dict()

        for (key1, value1), (key2, value2) in zip(expand_1.items(), expand_2.items()):
            out_key = key1 + " " + key2
            out_value = value1 + " " + value2
            out_dict[out_key] = out_value

        return out_dict

    def reduce(self, nodes: Sequence[Node]) -> Node:
        """Reduce the input nodes.

        Args:
            nodes (Sequence[Node]): Input 2 nodes.

        Returns:
            Node: Output 1 reduced node.
        """
        input_dicts = [nodes[0].value_dict, nodes[1].value_dict]
        value_dict = self.transform_reduce(input_dicts)
        output_node = Node(name=self.unique_name(), value_dict=value_dict, prev_nodes=nodes)
        return output_node

    def __call__(self, nodes: Sequence[Node], func) -> Node:
        """Call reduce operation.

        Args:
            nodes (Sequence[Node]): Input 2 nodes.
            func: reduce the input 2 nodes into 1 node

        Returns:
            Node: Output reduced node.
        """
        return func(nodes)
