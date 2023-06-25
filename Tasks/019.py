import time

def timing_decorator(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print("Time taken in seconds:", end - start)
    return wrapper

@timing_decorator
def my_function():
    time.sleep(1)

my_function()
