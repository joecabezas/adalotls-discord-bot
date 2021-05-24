import json
from pathlib import Path

from crawl_runner import CrawlRunner

class AdalotlMetadata:
    BASE_DATA_DIR='data/adalotls'

    def __init__(self):
        Path("data/adalotls").mkdir(parents=True, exist_ok=True)

    def get(self, number):
        try:
            with open(f"{self.BASE_DATA_DIR}/{number}.json") as f:
                return json.load(f)
        except FileNotFoundError as e:
            pass

        #at this point the json file does not exist, so we
        #need to get it from the transaction using the scraper

        runner = CrawlRunner()
        result = runner.run(number)

        if not result:
            return None

        return result[0]
