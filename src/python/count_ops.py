#!python3
import time

import numpy as np


def count_ops(job_duration: float, array_s: int = 64) -> int:
    """
    Count how many matmul ops could be calculated
    for a given time.

    PARAMETERS
    ----------
    job_duration: float
        Duration of the operations.

    array_s: int
        Shape of the 2d-array `(array_s, array_s)`
        randomly generated with `np.float64` dtype.

    RETURN
    ------
    int
        Operations count.
    """
    ops_count = 0
    start_time = time.perf_counter()
    while time.perf_counter() - start_time < job_duration:
        a = np.random.rand(array_s, array_s)
        x = np.random.rand(array_s, array_s)
        b = np.random.rand(array_s, array_s)
        _ = np.matmul(a, x) + b
        ops_count += 1
    return ops_count
