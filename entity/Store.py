from typing import Dict

from entity.BaseStorage import BaseStorage
from entity.exception import ToManyItemsError


class Store(BaseStorage):
    def __init__(self, items: Dict, capacity: int = 100):
        super().__init__(items, capacity)

    def add(self, name: str, amount: int) -> None:
        if self.get_unique_items_count() >= 5:
            raise ToManyItemsError
        super().add(name, amount)
