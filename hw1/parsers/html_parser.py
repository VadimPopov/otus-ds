import json
import pandas as pd
from bs4 import BeautifulSoup


class HtmlParser(object):
    '''
    Class for data parsing to extract attributes (fields)
    '''

    def __init__(self, fields=None):
        self.fields = fields

    def parse(self, infile, outfile):
        """
        Parses HTML text and extracts field values
        :param infile: name of the input file with HTML text
        :param outfile: name of the output file
        """

        # preprocessing raw data

        with open(infile, 'rb') as f:
            soup = BeautifulSoup(f, 'html.parser')
            json_lst = []

            for scr in soup.find_all('script'):
                if 'list' in scr.text:

                    try:

                        # extracting dictionaries with user data

                        txt = scr.text.split('list')[1]
                        start = txt.index('[{"c')
                        end = txt.index(']})') + 1
                        kagglers = json.loads(txt[start:end])
                        json_lst.extend([*kagglers])

                    except:

                        # skipping problematic dictionaries

                        continue

            print('{} entries added'.format(len(json_lst)))

        # editing resulting JSON dictionaries

        keys_to_drop = ['currentRanking', 'thumbnailUrl', 'userId', 'userUrl']

        for kaggler in json_lst:

            # adding an extra field for total number of medals

            kaggler['totalMedals'] = kaggler['totalBronzeMedals'] +\
                                     kaggler['totalGoldMedals'] +\
                                     kaggler['totalSilverMedals']

            # deleting unimportant data

            for key in keys_to_drop:
                del kaggler[key]

        # saving the list of dictionaries to a CSV file

        pd.DataFrame(json_lst).to_csv(outfile, index=False)
