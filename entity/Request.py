from typing import Dict

from entity.AbstractStorage import AbstractStorage
from entity.exception import InvalidRequestError, InvalidDepartureError, InvalidDestinationError


class Request:
    def __init__(self, storages: Dict[str, AbstractStorage], waybill: str):
        split_waybill = waybill.lower().split(" ")
        if len(split_waybill) != 7:
            raise InvalidRequestError

        self.amount = int(split_waybill[1])
        self.product = split_waybill[2]
        self.destination = split_waybill[6]
        self.departure = split_waybill[4]

        if self.departure not in storages:
            raise InvalidDepartureError

        if self.destination not in storages:
            raise InvalidDestinationError
