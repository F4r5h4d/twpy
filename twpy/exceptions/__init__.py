
class IndexError(Exception):
    def __init__(self, message):
        super().__init__(message)


class ConnectionTimeout(Exception):
    def __init__(self, message):
        super().__init__(message)


class InvalidValue(Exception):
    def __init__(self, message):
        super().__init__(message)
