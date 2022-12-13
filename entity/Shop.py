from typing import Dict

from entity.BaseStorage import BaseStorage


class Shop(BaseStorage):
    def __init__(self, items: Dict, capacity: int = 20):
        super().__init__(items, capacity)
