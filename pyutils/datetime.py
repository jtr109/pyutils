import datetime


def timestamp(t: datetime.datetime) -> int:
    ''' Convert Datetime into Timestamp in Millisecond
    '''
    return int(t.timestamp() * 1000)
