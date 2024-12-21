#!/bin/bash
# Refresh csv file with headers
echo "Implementation, n=500, n=1000, n=2500, n=5000, n=10000" > results.csv

# setup Cython build
python3 setup.py build_ext --inplace 1>/dev/null

# benchmark and write to csv
python3 cy_test.py
pypy primes.py PyPy
python3 primes.py CPython
jython primes.py Jython

echo "Benchmark complete. Output in results.csv"