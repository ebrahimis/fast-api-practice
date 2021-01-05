class BaseError(Exception):
    """
    Base class for all app exceptions.
    """
    pass


class BusinessError(BaseError):
    """
    Base class for all exceptions that raises when
    an operation attempts to break business rule.

    :param key: A unique key that identifies the error.
    :param description: Description of the error.
    """

    def __init__(self, description):
        self.description = description


class NotExistError(BaseError):
    """
    Base class for all exceptions that raises when an operation
    attempts to manipulate nonexistent resource.

    :param description: Description of the error.
    """

    def __init__(self, description):
        self.description = description


class UnauthorizedError(BaseError):
    """
    Base class for all exceptions that raises when a user
    attempts to make unauthorized operation.

    :param description: Description of the error.
    """

    def __init__(self, description):
        self.description = description
