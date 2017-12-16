from abc import ABC, abstractmethod
from typing import List, Optional

from exchange import Exchange
from spread_detection import Spread


class UpdateAction(ABC):
    def __init__(self, spread_threshold: Optional[int]=None) -> None:
        self.threshold = spread_threshold or 0

    @abstractmethod
    def run(self, spreads: List[Spread], exchanges: List[Exchange], timestamp: float) -> None:
        raise NotImplementedError
