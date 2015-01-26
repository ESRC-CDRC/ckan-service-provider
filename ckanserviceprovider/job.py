import web


def async(check_conflict=lambda x, y: False):
    """ A decorator to mark functions that can be execute asynchronously.
        :check_conflict: a function taking two dicts as meta information about the
        jobs and should True/False when two job should/not run concurrently.
    """
    def async_wrapper(func):
        """ A wrapper."""
        web.async_types[func.__name__] = (func, check_conflict)
        return func
    return async_wrapper


def sync(func):
    web.sync_types[func.__name__] = func
    return func
