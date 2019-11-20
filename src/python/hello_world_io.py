#!python3
import time

import requests


def fetch_url(session: requests.Session, url: str):
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
    urls = [
        "http://localhost:5000/kittens2.webm",
        "http://localhost:5000/kittens.webm",
        "http://localhost:5000"
    ] * 3

    with requests.Session() as sess:
        urls_data = []
        for url in urls:
            data = fetch_url(session=sess, url=url)
            urls_data.append(data)
            load_time = time.perf_counter()
            # print(
            #     "Loaded {} ({:.2f} MB) in {:.2f} ms".format(
            #         url, len(data)/(1 << 20), (load_time - start_time) * 1000))
        finish_time = time.perf_counter()
        print(
            "Finished all jobs in {:.2f} ms".format((finish_time - start_time) * 1000))


if __name__ == "__main__":
    main()
