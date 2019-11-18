#!python3
import multiprocessing as mp
import sys
import time
from functools import partial

import numpy as np


def count_ops(worker_no: int, job_duration: float, sleep_duration: float = 0.):
    ops_count = 0
    start_time = time.time()
    while time.time() - start_time < job_duration:
        a = np.random.rand(64, 64)
        x = np.random.rand(64, 64)
        b = np.random.rand(64, 64)
        _ = np.matmul(a, x) + b
        ops_count += 1
        if not sleep_duration:
            continue
        time.sleep(sleep_duration)
    if "-q" not in sys.argv:
        print(
            "Worker {}: Finished with {}k operations, about {:.3f}k operations per second".format(
                worker_no, ops_count / 1000, (ops_count / 1000) / job_duration))
    return ops_count


def main():
    start_time = time.time()
    n_jobs = 6
    job_duration = 1.
    sleep_duration = 0.

    with mp.Pool(processes=n_jobs) as pool:
        ops_counts = pool.map(
            partial(
                count_ops, job_duration=job_duration, sleep_duration=sleep_duration),
            range(n_jobs))
        finish_time = time.time()
    ops_count_total = sum(ops_counts)
    print(
        "Finished all jobs, totalling {}k operations, about {:.3f}k operations per second".format(
            ops_count_total / 1000, (ops_count_total / 1000) / (finish_time - start_time))
    )


if __name__ == "__main__":
    main()
