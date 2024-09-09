from typing import Any, Optional, Tuple

class Node:

    def __init__(self, data: Any, parent: Optional["Node"]) -> None:
        self.data = data
        self.balanceFactor =0
        self.left: Optional["Node"] = None
        self.right: Optional["Node"] = None
        self.parent: Optional["Node"] = None
        self.height = 1