from datetime import datetime, timezone


def datetime_utcnow():
    """
    Function to get the current time in UTC because of deprecated datetime.utcnow() function.
    :return: Function returning a current time by utc.
    """
    def _datetime_utcnow():
        return datetime.now(tz=timezone.utc)
    return _datetime_utcnow
