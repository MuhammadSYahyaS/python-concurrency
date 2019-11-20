#!python3
import multiprocessing as mp
import time
from functools import partial

import requests


def fetch_url(url: str, session: requests.Session):
    start_time = time.perf_counter()
    with session.request("GET", url) as response:
        data = response.content
        finish_time = time.perf_counter()
        # print(
        #     "Finished request {} in {:.2f} ms".format(
        #         url, (finish_time - start_time) * 1000
        #     ))
        return data


def main():
    start_time = time.perf_counter()
    n_jobs = 6
    urls = [
        "http://localhost:5000/kittens2.webm",
        "http://localhost:5000/kittens.webm",
        "http://localhost:5000"
    ] * 3

    with mp.Pool(processes=n_jobs) as pool, requests.Session() as sess:
        urls_data = pool.map(partial(fetch_url, session=sess), urls)
        finish_time = time.perf_counter()
        print(
            "Finished all jobs in {:.2f} ms".format((finish_time - start_time) * 1000))


if __name__ == "__main__":
    main()
