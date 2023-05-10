import time


def my_func():
    start_time = time.time()
    s = 0
    for i in range(1, n+1):
        s += i
    end_time = time.time()
    return s, round(end_time-start_time, 3)


n = 5
print(my_func())
