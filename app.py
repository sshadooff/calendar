from flask import Flask

app = Flask(__name__)


API_ROOT = "/api/v1/calendar/"
EVENT_API_ROOT = API_ROOT + "/event"


@app.route(EVENT_API_ROOT + "/", methods=["POST"])
def create():
    pass


@app.route(EVENT_API_ROOT + "/", methods=["GET"])
def list():
    pass


@app.route(EVENT_API_ROOT + "/<int:_id>", methods=["GET"])
def read(_id: int):
    pass


@app.route(EVENT_API_ROOT + "/<int:_id>", methods=["PUT"])
def update(_id: int):
    pass


@app.route(EVENT_API_ROOT + "/<int:_id>", methods=["DELETE"])
def delete(_id: int):
    pass


if __name__ == "__main__":
    app.run()
