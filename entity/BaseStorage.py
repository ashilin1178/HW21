from entity.AbstractStorage import AbstractStorage
from typing import Dict

from entity.exception import NotEnoughSpaceError, UnknownProductError, NotEnoughProductError


class BaseStorage(AbstractStorage):

    def __init__(self, items: Dict, capacity: int):
        self._items = items
        self._capacity = capacity

    def add(self, name: str, amount: int) -> None:
        if self.get_free_space() <= amount:
            raise NotEnoughSpaceError
        else:
            self._items[name] = self._items.get(name, 0) + amount

    def remove(self, name: str, amount: int) -> None:
        if self._items[name] is None:
            raise UnknownProductError

        elif self._items[name] <= amount:
            raise NotEnoughProductError

        else:
            self._items[name] -= amount

        if self._items[name] == 0:
            self._items.pop(name)

    def get_free_space(self) -> int:
        return self._capacity - sum(self._items.values())

    def get_items(self) -> Dict:
        return self._items

    def get_unique_items_count(self) -> int:
        return len(self._items)
