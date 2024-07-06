import functools


def log(filename=None):
    """
        Декоратор для логирования информации о вызове функции.

        Параметры:
        - filename: str, необязательный. Имя файла для записи логов.
                    Если не указан, логи выводятся в консоль.

        Логирует:
        - Имя функции и результат выполнения при успешной операции.
        - Имя функции, тип возникшей ошибки и входные параметры при ошибке.
        """
    def decorator_log(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                log_message = f"{func.__name__} ok\n"
                if filename:
                    with open(filename, "a") as f:
                        f.write(log_message)
                else:
                    print(log_message)
                return result
            except Exception as e:
                log_message = f"{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}\n"
                if filename:
                    with open(filename, "a") as f:
                        f.write(log_message)
                else:
                    print(log_message)
                raise

        return wrapper

    return decorator_log
