import copy
from typing import Any, Mapping, Sequence

from uniflow.node import Node
from uniflow.op.op import Op


class ExpandOp(Op):
    """Expand operation class"""

    def __init__(self, name: str) -> None:
        super().__init__(name)

    def transform_expand(self, value_dict: Mapping[str, Any], idx: int) -> Sequence[Mapping[str, Any]]:
        """Transform value dict.

        Args:
            value_dict (Mapping[str, Any]): Input root dict.
            idx (int): the index where the root node is split

        Returns:
            Sequence[Mapping[str, Any]]: Output the value dicts of 2 nodes .
        """

        dict_1 = {k: value_dict[k] for k in list(value_dict)[:idx]}
        dict_2 = {k: value_dict[k] for k in list(value_dict)[idx:]}
        out_dicts = [copy.deepcopy(dict_1), copy.deepcopy(dict_2)]

        return out_dicts

    def divide_half(self, root: Node) -> Sequence[Node]:
        """Expand the root node.

        Args:
            root (Node): Input root node.

        Returns:
            Sequence[Node]: Output nodes.
        """
        value_dicts = self.transform_expand(root.value_dict[0], len(root.value_dict[0]) // 2)
        expand_1 = Node(name=self.unique_name(), value_dict=value_dicts[0], prev_nodes=[root])
        expand_2 = Node(name=self.unique_name(), value_dict=value_dicts[1], prev_nodes=[root])
        output_nodes = [expand_1, expand_2]
        return output_nodes

    def __call__(self, root: Node, func) -> Sequence[Node]:
        """Call expand operation.

        Args:
            root (Node): Input root node.
            func: the function which divide the root node into 2 nodes

        Returns:
            Sequence[Node]: Output nodes.
        """
        return func(root)
