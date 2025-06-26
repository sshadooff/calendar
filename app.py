from flask import Flask, request
from event import Event
from logic import EventLogic

app = Flask(__name__)

_event_logic = EventLogic()


class ApiException(Exception):
    pass


def _from_raw(raw_event: str) -> Event:
    parts = raw_event.split("|")
    if len(parts) == 3:
        event = Event(id=None, date=parts[0], header=parts[1], text=parts[2])
        return event
    elif len(parts) == 4:
        event = Event(id=parts[0], date=parts[1], header=parts[2], text=parts[3])
        return event
    else:
        raise ApiException(f"invalid RAW note data {raw_event}")


def _to_raw(event: Event) -> str:
    if event.id is None:
        return f"{event.date}|{event.header}|{event.text}"
    else:
        return f"{event.id}|{event.date}|{event.header}|{event.text}"


API_ROOT = "/api/v1/calendar/"
EVENT_API_ROOT = API_ROOT + "/event"


@app.route(EVENT_API_ROOT + "/", methods=["POST"])
def create():
    try:
        data = request.get_data().decode("utf-8")
        event = _from_raw(data)
        _id = _event_logic.create(event)
        return f"create an event with id: {_id}", 201
    except Exception as ex:
        return f"failed to CREATE with: {ex}", 404


@app.route(EVENT_API_ROOT + "/", methods=["GET"])
def list():
    try:
        events = _event_logic.list()
        raw_event = ""
        for event in events:
            raw_event += _to_raw(event) + "\n"
        return raw_event, 200
    except Exception as ex:
        return f"failed to LIST with: {ex}", 404


@app.route(EVENT_API_ROOT + "/<_id>/", methods=["GET"])
def read(_id: str):
    try:
        event = _event_logic.read(_id)
        raw_event = _to_raw(event)
        return raw_event, 200
    except Exception as ex:
        return f"failed to READ with: {ex}", 404


@app.route(EVENT_API_ROOT + "/<_id>/", methods=["PUT"])
def update(_id: str):
    try:
        data = request.get_data().decode("utf-8")
        event = _from_raw(data)
        _event_logic.update(_id, event)
        return "updated an event", 200
    except Exception as ex:
        return f"failed to UPDATE with: {ex}", 404


@app.route(EVENT_API_ROOT + "/<_id>/", methods=["DELETE"])
def delete(_id: str):
    try:
        _event_logic.delete(_id)
        return "deleted an event", 200
    except Exception as ex:
        return f"failed to DELETE with: {ex}", 404


if __name__ == "__main__":
    app.run()
