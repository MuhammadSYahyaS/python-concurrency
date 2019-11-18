#!python3
import multiprocessing as mp
import sys
import time

import numpy as np


class HelloWorldMP(mp.Process):
    def __init__(self, job_duration: float, sleep_duration: float = 0.):
        mp.Process.__init__(self)
        self.job_duration = job_duration
        self.sleep_duration = sleep_duration
        self.ops_count = mp.Value("i", 0)

    def run(self):
        start_time = time.time()
        while time.time() - start_time < self.job_duration:
            a = np.random.rand(64, 64)
            x = np.random.rand(64, 64)
            b = np.random.rand(64, 64)
            _ = np.matmul(a, x) + b
            self.ops_count.value += 1
            if not self.sleep_duration:
                continue
            t_start = time.time()
            time.sleep(self.sleep_duration)
            true_sleep_duration = time.time() - t_start
            print(
                "Hello from {} after slept {:.2f} s".format(self.name, true_sleep_duration))
        if "-q" not in sys.argv:
            print(
                "{} finished with {}k operations, about {:.3f}k operations per second".format(
                    self.name, self.ops_count.value / 1000, (self.ops_count.value / 1000) / self.job_duration))


def main():
    start_time = time.time()
    n_jobs = 6
    job_duration = 1.
    sleep_duration = 0.

    processes_list = []

    for _ in range(n_jobs):
        processes_list.append(
            HelloWorldMP(
                job_duration=job_duration,
                sleep_duration=sleep_duration))
    for t in processes_list:
        t.start()
    for t in processes_list:
        t.join()
    ops_counts = [t.ops_count.value for t in processes_list]
    finish_time = time.time()
    ops_count_total = sum(ops_counts)
    print(
        "Finished all jobs, totalling {}k operations, about {:.3f}k operations per second".format(
            ops_count_total / 1000, (ops_count_total / 1000) / (finish_time - start_time))
    )


if __name__ == "__main__":
    main()
