from datetime import date


class Event:
    def __init__(self, id: int, date: date, header: str, text: str):
        self.id = id
        self.date = date
        self.header = header
        self.text = text
