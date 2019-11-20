#!python3
import multiprocessing as mp
import sys
import time

from count_ops import count_ops


class HelloWorldMP(mp.Process):
    def __init__(self, job_duration: float, array_s: int = 64):
        mp.Process.__init__(self)
        self.job_duration = job_duration
        self.array_s = array_s
        self.ops_count = mp.Value("i", 0)

    def run(self):
        start_time = time.perf_counter()
        self.ops_count.value = count_ops(
            job_duration=self.job_duration, array_s=self.array_s)
        finish_time = time.perf_counter()
        if "-q" not in sys.argv:
            print(
                "{} finished with {}k operations, about {:.3f}k operations per second".format(
                    self.name, self.ops_count.value / 1000,
                    (self.ops_count.value / 1000) / (finish_time - start_time)))


def main():
    start_time = time.perf_counter()
    n_jobs = 6
    job_duration = 1.

    processes_list = []

    for _ in range(n_jobs):
        processes_list.append(
            HelloWorldMP(
                job_duration=job_duration))
    for t in processes_list:
        t.start()
    for t in processes_list:
        t.join()
    ops_counts = [t.ops_count.value for t in processes_list]
    finish_time = time.perf_counter()
    ops_count_total = sum(ops_counts)
    print(
        "Finished all jobs, totalling {}k operations, about {:.3f}k operations per second".format(
            ops_count_total / 1000, (ops_count_total / 1000) / (finish_time - start_time))
    )


if __name__ == "__main__":
    main()
