import logging
import requests
import time


logger = logging.getLogger(__name__)


class Scraper(object):
    '''
    Class for scraping data off the oficial Kaggle site
    '''

    def __init__(self, skip_objects=None):
        self.skip_objects = skip_objects

    def scrape_process(self, storage):
        '''
        Scrapes user data from the Kaggle leaderboard
        :param storage: object for saving scraped data
        '''

        base_url = 'https://www.kaggle.com/rankings'
        items_per_page = 20
        n_users = 3000
        for i in range(1, n_users // items_per_page + 1):
            url = base_url + '?page={}'.format(i)
            response = requests.get(url)

            if not response.ok:
                logger.error(response.text)
                time.sleep(.3)
                continue

            else:
                if i % 15 == 0:
                    print('getting page {}/{}'.format(i, n_users // items_per_page))
                data = response.text
                storage.append_data([bytes(data, 'utf8')])
                time.sleep(.3)
