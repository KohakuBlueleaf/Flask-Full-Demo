from datetime import datetime


def utc_time():
    return int(datetime.now().timestamp())
