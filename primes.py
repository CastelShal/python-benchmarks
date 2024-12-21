import sys
import timeit

environment = sys.argv[1]

primes = """
def primes(nb_primes):
    nb_primes = min(nb_primes, 90000)
    p = []
    current = 0  # The current number of elements in p.
    n = 2
    while current < nb_primes:
        # Is n prime?
        for i in p[:current]:
            if n % i == 0:
                break
        else:
            p.append(n)
            current += 1
        n += 1

    return p
"""

sizes = [500, 1000, 2500, 5000, 10000]
exec_times = []
for size in sizes:
    exec_times.append(
        timeit.Timer("primes("+str(size)+")",primes)
        .repeat(5,1))

# We are only interested in the minimum execution time as any variance
# in runtime is likely caused by other competing processes as opposed to implementation efficiency
# Output is in seconds, rounded to 6 sigfigs, cast to string
min_exec_times = [str(round(min(times), 6)) for times in exec_times]

# append to file as csv
file = open("results.csv", "a")
file.write(environment + ',' + ",".join(min_exec_times) + "\n")
file.close()
