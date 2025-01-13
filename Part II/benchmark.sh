#!/bin/bash
# Refresh csv file with headers
echo "Implementation, n=5000, n=10000, n=20000, n=30000, n=50000, n=70000, n=100000" > results.csv

python3 parallelMerge.py
python3 sequentialMerge.py

echo "Benchmark complete. Output in results.csv"