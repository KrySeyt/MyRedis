from myasync import Coroutine

from myredis.application.gateways.values import ValuesStorage
from myredis.domain.key import Key
from myredis.domain.record import Record


class Get:
    def __init__(self, values_storage: ValuesStorage) -> None:
        self._values_storage = values_storage

    def __call__(self, key: Key) -> Coroutine[Record | None]:
        record = yield from self._values_storage.get(key)
        return record
