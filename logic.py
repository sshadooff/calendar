from typing import List
from event import Event
import db

HEADER_LIMIT = 30
TEXT_LIMIT = 200


class LogicException(Exception):
    pass


class EventLogic:
    def __init__(self):
        self._event_db = db.EventDB()

    def _validate_note(self, event: Event):
        if event is None:
            raise LogicException("note is None")
        if event.header is None or len(event.header) > HEADER_LIMIT:
            raise LogicException(f"title lenght > MAX: {HEADER_LIMIT}")
        if event.text is None or len(event.text) > TEXT_LIMIT:
            raise LogicException(f"text lenght > MAX: {TEXT_LIMIT}")

    def create(self, event: Event) -> str:
        self._validate_note(event)
        try:
            return self._event_db.create(event)
        except Exception as ex:
            raise LogicException(f"failed CREATE operation with: {ex}")

    def list(self) -> List[Event]:
        try:
            return self._event_db.list()
        except Exception as ex:
            raise LogicException(f"failed LIST operation with: {ex}")

    def read(self, _id: str) -> Event:
        try:
            return self._event_db.read(_id)
        except Exception as ex:
            raise LogicException(f"failed READ operation with: {ex}")

    def update(self, _id: str, note: Event):
        self._validate_note(note)
        try:
            return self._event_db.update(_id, note)
        except Exception as ex:
            raise LogicException(f"failed UPDATE operation with: {ex}")

    def delete(self, _id: str):
        try:
            return self._event_db.delete(_id)
        except Exception as ex:
            raise LogicException(f"failed DELETE operation with: {ex}")
