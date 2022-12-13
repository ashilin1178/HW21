from entity.AbstractStorage import AbstractStorage
from typing import Dict

from entity.Request import Request


class Curier:
    def __init__(self, request: Request, storages: Dict[str, AbstractStorage]):
        self._request = request
        self._to = storages[self._request.destination]
        self._from = storages[self._request.departure]

    def move(self):
        self._from.remove(name=self._request.product, amount=self._request.amount)
        print(f'Курьер забрал {self._request.amount} {self._request.product} из {self._request.departure}')

        print(f'Курьер везёт {self._request.amount} {self._request.product} из {self._request.departure} '
              f'в {self._request.destination}')

        self._to.add(name=self._request.product, amount=self._request.amount)
        print(
            f'Курьер доставил {self._request.amount} {self._request.product}  в {self._request.destination}')
