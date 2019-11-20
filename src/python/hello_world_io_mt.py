#!python3
import threading as mt
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


class FetchURL(mt.Thread):
    def __init__(self, session: requests.Session, url: str):
        mt.Thread.__init__(self)
        self.session = session
        self.url = url
        self.data = None

    def run(self):
        self.data = fetch_url(self.session, self.url)


def main():
    start_time = time.perf_counter()
    urls = [
        "http://localhost:5000/kittens2.webm",
        "http://localhost:5000/kittens.webm",
        "http://localhost:5000"
    ] * 3

    with requests.Session() as sess:
        threads_list = [FetchURL(session=sess, url=url) for url in urls]

        for t in threads_list:
            t.start()

        [t.join() for t in threads_list]

        urls_data = []
        for t, url in zip(threads_list, urls):
            data = t.data
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
