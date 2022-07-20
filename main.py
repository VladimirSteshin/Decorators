import datetime as dt
from application.db.people import get_employees as hr
from application.salary import calculate_salary as pay


def now():
    full = dt.datetime.now()
    return full.date()


if __name__ == '__main__':
    hr(now())
    pay(now())
