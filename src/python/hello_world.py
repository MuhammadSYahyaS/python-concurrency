#!python3
import time

from count_ops import count_ops


def main():
    start_time = time.perf_counter()
    job_duration = 1.
    ops_count = count_ops(job_duration=job_duration)
    finish_time = time.perf_counter()
    print(
        "Finished with {}k operations, about {:.3f}k operation per second".format(
            ops_count / 1000, (ops_count / 1000) / (finish_time - start_time)))


if __name__ == "__main__":
    main()
