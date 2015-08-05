# Cachee Monkey

A tiny Python library for caching the results of functions.

Currently uses `django.core.cache` for caching results, but could/should be made more flexible and non-hard-dependent on that.

## Usage

```
from cachee.mokney import cache_results, clear_result

# Cache the results of calls to a function, like so:

@cache_results
def make_me_a_sandwich(filling, bread="brown"):
    thing_which_takes_a_lot_of_effort_here()

make_me_a_sandwich("cheese") # The first call to the function happens as usual

# but subsequent calls just use the result from the cache
make_me_a_sandwich("cheese")
make_me_a_sandwich("cheese")
make_me_a_sandwich("cheese")
make_me_a_sandwich("cheese")

# If you call the function with different args or kwargs, then a real call is made to the function
make_me_a_sandwich("cucumber") # this triggers a real function call
make_me_a_sandwich("cucumber") # this uses the cache
make_me_a_sandwich("cheese", bread="white") # this triggers a real function call
make_me_a_sandwich("cheese", bread="white") # this uses the cache

# After a while you get sick of being given the same recycled sandwich each time you ask for the
# same one again, so you want to clear the cache

clear_result(make_me_a_sandwich, "cucumber")

# Now the next call to the function with those args/kwargs triggers a real call again, and you get
# a freshly-made sandwich

mmmm = make_me_a_sandwich("cucumber")

# and subsequent calls then use the cache again
stale = make_me_a_sandwich("cucumber")
```


