




class OkraException(Exception):
    """The base exception class for all OkraException"""
    pass


class MissingAuthKeyError(OkraException):
    """
    We can't find the authentication/authorization key
    """
    pass


class InvalidMethodError(OkraException):
    """
    Http method error class
    """
    pass

class MissingRequiredDataError(OkraException):
    """
    Missing data error class
    """
    pass