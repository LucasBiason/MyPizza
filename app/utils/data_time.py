
from datetime import date, datetime


def date_to_db(data: str) -> str:
    if not data:
        return data
    return '-'.join(data.split('/')[::-1])
