import random
import timeit
from functools import partial

def merge(left, right):
    l_len = len(left)
    r_len = len(right)
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

if __name__ == "__main__":
    sizes = [5000, 10000, 20000, 30000, 50000, 70000, 100000]
    exec_times = []
    for size in sizes:
        data_unsorted = [ random.randint(0, size) for _ in range(size) ]
        exec_times.append(
            timeit.Timer(partial(merge_sort, data_unsorted))
            .repeat(5,1))

    min_exec_times = [str(round(min(times), 6)) for times in exec_times]

    # append to file as csv
    file = open("results.csv", "a")
    file.write(f"Sequential Merge Sort, {",".join(min_exec_times)}\n")
    file.close()