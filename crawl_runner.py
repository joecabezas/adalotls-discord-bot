import sys
import os
import logging

from scrapyscript import Job, Processor

import sys
sys.path.append("stakepoolcentral-scraper/stakepoolcentral")
from stakepoolcentral.spiders.tx_metadata_searchresults import TxMetadataSearchresultsSpider

class CrawlRunner:
    def run(self, number):
        spider = TxMetadataSearchresultsSpider

        job = Job(spider, number=number)
        processor = Processor(settings={
            'ITEM_PIPELINES': {
                'stakepoolcentral.pipelines.StakepoolcentralPipeline': 300,
                }
            })
        return processor.run(job)
