from entity.AbstractStorage import AbstractStorage
from typing import Dict


class BaseStorage(AbstractStorage):

    def __init__(self, items: Dict, capacity: int):
        self._items = items
        self._capacity = capacity

    def add(self, name: str, amount: int) -> None:
        if self.get_free_space() >= amount:
            self._items[name] = self._items.get(name, 0) + amount
        else:
            # TODO "нет свободного места"
            ...

    def remove(self, name: str, amount: int) -> None:
        if self._items[name] >= amount:
            self._items[name] -= amount
        else:
            # TODO "нет данного количества товара"
            ...

    def get_free_space(self) -> int:
        return self._capacity - sum(self._items.values())

    def get_items(self) -> Dict:
        return self._items

    def get_unique_items_count(self) -> int:
        return len(self._items)
