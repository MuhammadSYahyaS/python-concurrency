#!python3
import multiprocessing as mp
import sys
import time
from functools import partial

from count_ops import count_ops


def count_ops_worker(worker_no: int, job_duration: float, array_s: int = 64):
    start_time = time.perf_counter()
    ops_count = count_ops(
        job_duration=job_duration, array_s=array_s)
    finish_time = time.perf_counter()
    if "-q" not in sys.argv:
        print(
            "Worker {}: Finished with {}k operations, about {:.3f}k operations per second".format(
                worker_no, ops_count / 1000, (ops_count / 1000) / (finish_time - start_time)))
    return ops_count


def main():
    start_time = time.perf_counter()
    n_jobs = 6
    job_duration = 1.

    with mp.Pool(processes=n_jobs) as pool:
        ops_counts = pool.map(
            partial(
                count_ops_worker, job_duration=job_duration),
            range(n_jobs))
        finish_time = time.perf_counter()
    ops_count_total = sum(ops_counts)
    print(
        "Finished all jobs, totalling {}k operations, about {:.3f}k operations per second".format(
            ops_count_total / 1000, (ops_count_total / 1000) / (finish_time - start_time))
    )


if __name__ == "__main__":
    main()
