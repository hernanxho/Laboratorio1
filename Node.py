from typing import Any, Optional, Tuple

class Node:

    def _init_(self, data: Any) -> None:
        self.data = data
        self.left: Optional["Node"] = None
        self.right: Optional["Node"] = None