import time

current_time = time.time()
print(current_time)


def speed_calc_decorator(function):
    def wrapper_function():
        t_start = time.time()
        function()
        t_finish = time.time()
        speed = t_finish - t_start
        print(f"{function.__name__} run speed: {speed}")

    return wrapper_function()


def fast_function():
    for i in range(10000000):
        i * i


def slow_function():
    for i in range(100000000):
        i * i


speed_calc_decorator(fast_function)
speed_calc_decorator(slow_function)

