#!python3
import time

import numpy as np


class HelloWorld:
    def __init__(self, job_duration: float, sleep_duration: float = 0.):
        self.job_duration = job_duration
        self.sleep_duration = sleep_duration
        self.ops_count = 0

    def run(self):
        start_time = time.time()
        while time.time() - start_time < self.job_duration:
            a = np.random.rand(64, 64)
            x = np.random.rand(64, 64)
            b = np.random.rand(64, 64)
            self.ops_count += 1
            if not self.sleep_duration:
                continue
            t_start = time.time()
            time.sleep(self.sleep_duration)
            true_sleep_duration = time.time() - t_start
            print(
                "Hello after slept {:.2f} s".format(true_sleep_duration))


def main():
    start_time = time.time()
    job_duration = 1.
    sleep_duration = 0.

    hello_world = HelloWorld(
        job_duration=job_duration,
        sleep_duration=sleep_duration)
    hello_world.run()
    finish_time = time.time()
    print(
        "Finished with {}k operations, about {:.3f}k operation per second".format(
            hello_world.ops_count / 1000, (hello_world.ops_count / 1000) / (finish_time - start_time)))


if __name__ == "__main__":
    main()
