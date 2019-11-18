#!python3
import asyncio
import time

import aiohttp


async def fetch(session: aiohttp.ClientSession, url: str):
    start_time = time.time()
    async with session.request("GET", url) as response:
        data = await response.read()
        finish_time = time.time()
        # print(
        #     "Finished request {} in {:.2f} ms".format(
        #         url, (finish_time - start_time) * 1000
        #     ))
        return data


async def async_main():
    start_time = time.time()
    urls = [
        "http://localhost:5000/kittens2.webm",
        "http://localhost:5000/kittens.webm",
        "http://localhost:5000"
    ] * 3
    async with aiohttp.ClientSession() as sess:
        futs = [fetch(session=sess, url=url) for url in urls]
        urls_data = await asyncio.gather(*futs)
        for data, url in zip(urls_data, urls):
            urls_data.append(data)
            load_time = time.time()
            # print(
            #     "Loaded {} ({:.2f} MB) in {:.2f} ms".format(
            #         url, len(data)/(1 << 20), (load_time - start_time) * 1000))
        finish_time = time.time()
        print(
            "Finished all jobs in {:.2f} ms".format((finish_time - start_time) * 1000))


def main():

    loop = asyncio.get_event_loop()
    loop.run_until_complete(async_main())
    loop.close()


if __name__ == "__main__":
    main()
