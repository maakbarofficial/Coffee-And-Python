import time


def cache(func):
    cache_value = {}
    print(cache_value)

    def wrapper(*args, **kwargs):
        if args in cache_value:
            return cache_value[args]
        result = func(*args)
        cache_value[args] = result
        return result

    return wrapper


@cache
def long_running_function(a, b):
    time.sleep(4)
    return a + b


print(long_running_function(1, 2))
print(long_running_function(5, 2))
