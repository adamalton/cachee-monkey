# STANDARD LIB
from functools import wraps
import hashlib

# LIBRARIES
from django.core.cache import cache


def cache_results(function_or_cache_time):
    """ A decorator to cache the result of a function.  Results are cached separatly for each
        variation of args/kwargs passed to the function.

        To cache the results of a function for as long as possible:

        @cache_results
        def my_func(a, b, c=None):
            things()

        To cache the results of a function for 1 hour:

        @cache_results(3600)
        def my_func(a, b, c=None):
            things()
    """
    def decorator(function):
        """ This is the actual decorator, as the outer function is just a wrapper to allow it to be
            called with or without a cache time specified.
        """
        @wraps(function)
        def replacement(*args, **kwargs):
            cache_key = _get_cache_key(function, args, kwargs)
            result = cache.get(cache_key)
            if result is None:
                result = function(*args, **kwargs)
                cache.set(cache_key, cache_time)
            return result
        return replacement

    if callable(function_or_cache_time):
        # If the decorator has been called without a cache time specified
        cache_time = None
        return decorator(function_or_cache_time)

    cache_time = function_or_cache_time
    return decorator


def clear_result(function, args, kwargs):
    """ Clear the cache entry for the given function and the given args and kwargs. """
    key = _get_cache_key(function, args, kwargs)
    cache.delete(key)


def _get_cache_key(function, args=(), kwargs=None):
    """ Given a function and the args/kwargs passed to it, return a string of they key to
        cache it under.
    """
    kwargs = kwargs or {}
    key_hash = hashlib.md5()
    key_hash.update(function.__name__, function.__module__)
    return key_hash.hexdigest()

