import math
import multiprocessing
import random
import sys
import timeit
from functools import partial


def merge(*args):
    left, right = args[0] if len(args) == 1 else args
    l_len, r_len = len(left), len(right)
    l, r = 0, 0
    merged = []
    while l < l_len and r < r_len:
        if left[l] <= right[r]:
            merged.append(left[l])
            l += 1
        else:
            merged.append(right[r])
            r += 1
    if l == l_len:
        merged.extend(right[r:])
    else:
        merged.extend(left[l:])
    return merged

def merge_sort(data):
    length = len(data)
    if length <= 1:
        return data
    middle = length // 2
    left = merge_sort(data[:middle])
    right = merge_sort(data[middle:])
    return merge(left, right)

def merge_sort_parallel(data):
    processes = multiprocessing.cpu_count()
    pool = multiprocessing.Pool(processes=processes)
    size = int(math.ceil(float(len(data)) / processes))
    data = [data[i * size:(i + 1) * size] for i in range(processes)]
    data = pool.map(merge_sort, data)
    while len(data) > 1:
        extra = data.pop() if len(data) % 2 == 1 else None
        data = [(data[i], data[i + 1]) for i in range(0, len(data), 2)]
        data = pool.map(merge, data) + ([extra] if extra else [])
    return data[0]


if __name__ == "__main__":
    sizes = [5000, 10000, 20000, 30000, 50000, 70000, 100000]
    exec_times = []
    for size in sizes:
        data_unsorted = [ random.randint(0, size) for _ in range(size) ]
        exec_times.append(
            timeit.Timer(partial(merge_sort_parallel, data_unsorted))
            .repeat(5,1))

    min_exec_times = [str(round(min(times), 6)) for times in exec_times]

    # append to file as csv
    file = open("results.csv", "a")
    file.write(f"Parallel Merge Sort, {",".join(min_exec_times)}\n")
    file.close()
