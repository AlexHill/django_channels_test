import argparse
import concurrent.futures
import random
import time

import requests
import statistics

random.seed(0)


def load_url(url):
    r = requests.get(url)
    return r.elapsed


def run_test(concurrency, samples):
    start_time = time.time()
    with concurrent.futures.ThreadPoolExecutor(max_workers=concurrency) as executor:
        futures = [
            executor.submit(load_url, f'http://localhost:8000/delay/{int(1000 * (random.random()**2))}/')
            for _ in range(samples)
        ]
        elapsed = [f.result().total_seconds() for f in concurrent.futures.as_completed(futures)]

    print(f"Elapsed:  {time.time() - start_time}")
    print(f"Mean:     {statistics.mean(elapsed)}")
    print(f"Median:   {statistics.median(elapsed)}")
    print(f"Stddev:   {statistics.stdev(elapsed)}")
    print(f"Variance: {statistics.variance(elapsed)}")


if __name__ == "__main__":
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("concurrency", type=int, help="The maximum number of simultaneous in-flight requests.")
    arg_parser.add_argument("requests", type=int, help="How many requests to make in total.")
    opts = arg_parser.parse_args()
    run_test(opts.concurrency, opts.requests)
