import logging
import sys
import pandas as pd

from scrapers.scraper import Scraper
from storages.file_storage import FileStorage
from parsers.html_parser import HtmlParser
from stat_extractors.stat_extractor import StatExtractor

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


SCRAPED_FILE = 'raw_kaggle_data.txt'
TABLE_FORMAT_FILE = 'kaggle_processed.csv'


def gather_process():
    logger.info("gather")
    storage = FileStorage(SCRAPED_FILE)
    scraper = Scraper()
    scraper.scrape_process(storage)


def convert_data_to_table_format():
    logger.info("transform")
    parser = HtmlParser()
    parser.parse(SCRAPED_FILE, TABLE_FORMAT_FILE)


def stats_of_data():
    logger.info("stats")
    stat_extractor = StatExtractor()
    stat_extractor.extract_stats(TABLE_FORMAT_FILE)


if __name__ == '__main__':
    logger.info("Work started")

    if sys.argv[1] == 'gather':
        gather_process()

    elif sys.argv[1] == 'transform':
        convert_data_to_table_format()

    elif sys.argv[1] == 'stats':
        stats_of_data()

    logger.info("Work ended")
