import crawler
import time
import sys


def main():
    args = int(sys.argv[1])
    runCrawler(args)    

def runCrawler(times):

    print(f"------ Start crawler runner with frequency: {times} ------")
    start = time.time()

    for i in range(times):
        crawler.runCrawler()

    end = time.time()
    elapsed_time = end - start
    print(f"------ Crawler runner ended ------")
    print(f"Elapsed time: {elapsed_time} seconds")

if __name__ == "__main__":
    main()