from datetime import datetime
from functools import wraps
from os import getcwd


def log_default(func):

    @wraps(func)
    def inner(*args, **kwargs):
        answer = func(*args, **kwargs)
        date = datetime.now().ctime()
        arguments = args, kwargs
        for_log = f'{date} was called {func.__name__} with arguments {arguments} result = {answer}\n'
        with open('logs_for_HW_1.log', 'a', encoding='UTF-8') as file:
            file.write(str(for_log))

        return answer

    return inner


def log_path(path=getcwd()):

    def decor(func):

        @wraps(func)
        def inner(*args, **kwargs):
            answer = func(*args, **kwargs)
            date = datetime.now().ctime()
            arguments = args, kwargs
            where = r'{}'.format(path)
            for_log = f'{date} in {where} was called {func.__name__} with arguments {arguments} result = {answer}\n'
            with open(path + '\logs_for_HW_2.log', 'a', encoding='UTF-8') as file:
                file.write(r'{}'.format(for_log))

            return answer

        return inner

    return decor
