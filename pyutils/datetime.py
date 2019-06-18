import datetime


def timestamp(t: datetime.datetime) -> int:
    return int(t.timestamp() * 1000)
