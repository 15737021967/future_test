import datetime
import calendar


def datetime_to_epoch(dt: datetime.datetime):
    return calendar.timegm(dt.utctimetuple())


def datetime_from_epoch(ts: int):

    return datetime.datetime.fromtimestamp(ts)
