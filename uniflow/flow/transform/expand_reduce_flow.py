from typing import Sequence, Dict, Any
from uniflow.node import Node
from uniflow.flow.flow import Flow
from uniflow.op.basic.expand_op import ExpandOp
from uniflow.op.basic.reduce_op import ReduceOp
from uniflow.constants import TRANSFORM
from uniflow.op.prompt import PromptTemplate


class ExpandReduceFlow(Flow):
    """Expand and Reduce Flow Class."""

    TAG = TRANSFORM

    def __init__(
            self,
            prompt_template: PromptTemplate,
            model_config: Dict[str, Any],
            ) -> None:
        super().__init__()
        self._expand_op = ExpandOp("expand_op")
        self._reduce_op = ReduceOp("reduce_op")

    def run(self, nodes: Sequence[Node]) -> Sequence[Node]:
        """Run flow.

        Args:
            nodes (Sequence[Node]): Nodes.

        Returns:
            Sequence[Node]: Nodes.
        """
        expanded = self._expand_op(nodes[0], self._expand_op.divide_half)
        reduced = self._reduce_op(expanded, self._reduce_op.reduce)
        return [reduced]
