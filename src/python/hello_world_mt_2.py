#!python3
import queue
import sys
import threading as mt
import time

from count_ops import count_ops


def count_ops_que(que: queue.Queue, job_duration: float, array_s: int = 64):
    start_time = time.perf_counter()
    ops_count = count_ops(
        job_duration=job_duration, array_s=array_s)
    que.put(ops_count)
    finish_time = time.perf_counter()
    if "-q" not in sys.argv:
        print(
            "Finished with {}k operations, about {:.3f}k operations per second".format(
                ops_count / 1000, (ops_count / 1000) / (finish_time - start_time)))


def main():
    start_time = time.perf_counter()
    n_jobs = 6
    job_duration = 1.

    threads_list = []
    que = queue.Queue()

    for _ in range(n_jobs):
        threads_list.append(
            mt.Thread(
                target=count_ops_que,
                kwargs={
                    "que": que,
                    "job_duration": job_duration}))
    for t in threads_list:
        t.start()
    for t in threads_list:
        t.join()
    ops_counts = []
    while True:
        try:
            ops_counts.append(que.get_nowait())
        except queue.Empty:
            break
    finish_time = time.perf_counter()
    ops_count_total = sum(ops_counts)
    print(
        "Finished all jobs, totalling {}k operations, about {:.3f}k operations per second".format(
            ops_count_total / 1000, (ops_count_total / 1000) / (finish_time - start_time))
    )


if __name__ == "__main__":
    main()
