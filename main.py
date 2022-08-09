from datetime import datetime
from application.db.people import get_employees as hr
from application.salary import calculate_salary as pay


def now():
    full = datetime.now()
    return full.date()


if __name__ == '__main__':
    print(hr(now()))
    print(pay(now()))
