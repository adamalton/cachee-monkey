# STANDARD LIB
from __future__ import absolute_import

# 3RD PARTY
from django.core.cache import cache
from django.test import TestCase

# CACHEE
from cachee.monkey import cache_results, clear_result

FUNCTION_CALLS = []


@cache_results
def cached_function(*args, **kwargs):
    global FUNCTION_CALLS
    FUNCTION_CALLS.append([args, kwargs])
    return [args, kwargs]


class CacheeTest(TestCase):

    def setUp(self):
        cache.clear()
        global FUNCTION_CALLS
        del FUNCTION_CALLS[:]

    def test_result_is_cached(self):
        # The first time we call our function it should get called
        assert len(FUNCTION_CALLS) == 0
        result = cached_function("a", b=True)
        self.assertEqual(len(FUNCTION_CALLS), 1)
        # Calling it again with the same args and kwargs should not call it again
        result2 = cached_function("a", b=True)
        self.assertEqual(len(FUNCTION_CALLS), 1)
        # but the result should be the same
        self.assertEqual(result, result2)
        # Calling the function with different args or kwargs should result in a new call
        result3 = cached_function("A", b=True)
        self.assertEqual(len(FUNCTION_CALLS), 2)
        result4 = cached_function("a", b=False)
        # And the results of those calls should be different
        self.assertNotEqual(result2, result3)
        self.assertNotEqual(result2, result4)
        self.assertNotEqual(result3, result4)

    def test_clear_result(self):
        """ Test the ability to clear a single result from the cache. """
        assert len(FUNCTION_CALLS) == 0
        cached_function("a", b=True)
        cached_function("a", b=False)
        self.assertEqual(len(FUNCTION_CALLS), 2)
        # Now making those same call`s again should not trigger real function calls
        cached_function("a", b=True)
        cached_function("a", b=False)
        self.assertEqual(len(FUNCTION_CALLS), 2)
        # Now if we clear the cache for just one of them, then it should trigger a real call
        clear_result(cached_function, "a", b=True)
        cached_function("a", b=True)
        self.assertEqual(len(FUNCTION_CALLS), 3)
        # But calling the function with the un-cleared args should not trigger a real call
        cached_function("a", b=False)
        self.assertEqual(len(FUNCTION_CALLS), 3)
