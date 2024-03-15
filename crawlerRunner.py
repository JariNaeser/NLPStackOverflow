import crawler
import time

def runCrawler(times):

    print(f"------ Start crawler runner with frequency: {times} ------")
    start = time.time()

    for i in range(times):
        crawler.runCrawler()

    end = time.time()
    elapsed_time = end - start
    print(f"------ Crawler runner ended ------")
    print(f"Elapsed time: {elapsed_time} seconds")

runCrawler(10)