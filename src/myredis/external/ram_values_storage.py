from typing import Any

from myasync import Coroutine

from myredis.application.interfaces.values import ValuesStorage
from myredis.domain.key import Key
from myredis.domain.record import Record

storage: dict[Key, Record[Any]] = {}
new: dict[Key, Record[Any]] = {}


class RAMValuesStorage(ValuesStorage):
    def set(self, key: Key, record: Record[Any]) -> Coroutine[None]:
        yield None

        storage[key] = record
        new[key] = record

    def set_records(self, records: dict[Key, Record[Any]]) -> Coroutine[None]:
        yield None

        storage.clear()
        storage.update(records)

    def get(self, key: Key) -> Coroutine[Record[Any] | None]:
        yield None

        record = storage.get(key)
        return record

    def pop_new(self) -> Coroutine[dict[Key, Record[Any]]]:
        global new  # noqa: PLW0603
        yield None

        new_records = new
        new = {}
        return new_records
