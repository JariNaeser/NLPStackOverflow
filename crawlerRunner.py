import crawler

def runCrawler(times):

    print(f"------ Start run crawler with frequency: {times} ------")

    for i in range(times):
        crawler.runCrawler()

    print(f"------ Crawler runner ended ------")

runCrawler(10)