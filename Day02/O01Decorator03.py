
import time
#import functools
def log_execution(func):

    # helps preserve the original functions metadata (like its name and docstring) when wrapping it with a decorator
    #@functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        print(f"[LOG] '{func.__name__}' at {time.ctime(start)}")

        result = func(*args, **kwargs)

        end = time.time()

        print(f"[LOG] '{func.__name__}' in {end - start:.4f} seconds")
        return result
    return wrapper


@log_execution    #  call to the log_execution with process_data as argument, and call the returned value of the
# log_execution (that is the wrapper function)
def process_data(data):
    time.sleep(2)
    return [d.upper() for d in data]    # list comprehension

"""
for d in data:
    d.upper()
"""

output = process_data(['python', 'genai', 'agenticai'])
print("Result :", output)
