import timeit
environment = "Cython"

sizes = [500, 1000, 2500, 5000, 10000]
exec_times = []
for size in sizes:
    exec_times.append(
        timeit.Timer(f"primes({size})","from primes import primes")
        .repeat(5,1))

# We are only interested in the minimum execution time as any variance
# in runtime is likely caused by other competing processes as opposed to implementation efficiency
# Output is in seconds, rounded to 6 sigfigs, cast to string
min_exec_times = [str(round(min(times), 6)) for times in exec_times]

# append to file as csv
with open("results.csv", "a") as file:
    file.write(f'{environment},' + ",".join(min_exec_times) + "\n")