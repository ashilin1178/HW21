class BaseError(Exception):
    message = "Неизвестная ошибка"


class NotEnoughSpaceError(BaseError):
    message = "Не достаточно места"


class UnknownProductError(BaseError):
    message = "Не известный товар"


class NotEnoughProductError(BaseError):
    message = "Не достаточно товара"


class InvalidRequestError(BaseError):
    message = "Не правильный запрос"


class InvalidDepartureError(BaseError):
    message = "Не правильное место назначения"


class InvalidDestinationError(BaseError):
    message = "Не правильно место убытия товара"


class ToManyItemsError(BaseError):
    message = "Превышение количества наименований товара"
