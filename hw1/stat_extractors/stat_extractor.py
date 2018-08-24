import pandas as pd


class StatExtractor(object):
    '''
    Class for extracting some stats from processed data
    '''

    def __init__(self):
        pass

    def extract_stats(self, infile):
        '''
        Extracts stats from the given file
        :param infile: name of the input CSV file
        '''

        df = pd.read_csv(infile)

        print('\n' + '=' * 27)
        print('Number of Kagglers by tier:')
        print('=' * 27 + '\n')
        print(df.groupby('tier').size())
        print('-' * 27)

        bronze = df.loc[df.totalBronzeMedals.values.argmax(), ['displayName',
                                                               'totalBronzeMedals',
                                                               'tier']].values
        silver = df.loc[df.totalSilverMedals.values.argmax(), ['displayName',
                                                               'totalSilverMedals',
                                                               'tier']].values
        gold = df.loc[df.totalGoldMedals.values.argmax(), ['displayName',
                                                           'totalGoldMedals',
                                                           'tier']].values
        total = df.loc[df.totalMedals.values.argmax(), ['displayName',
                                                        'totalMedals',
                                                        'tier']].values

        print('\n' + '=' * 33)
        print('Kagglers who won the most medals:')
        print('=' * 33 + '\n')
        print('Name: {}\tBronze medals won: {}\tTier: {}'.format(*bronze))
        print('Name: {}\t\tSilver medals won: {}\tTier: {}'.format(*silver))
        print('Name: {}\t\tGold medals won: {}\tTier: {}'.format(*gold))
        print('Name: {}\t\tTotal medals won: {}\tTier: {}'.format(*total))
        print('-' * 65)

        print('\n' + '=' * 57)
        print('Average number of medals won by competitors in each tier:')
        print('=' * 57 + '\n')
        print(df.groupby('tier')[['totalGoldMedals', 'totalSilverMedals',
                            'totalBronzeMedals', 'totalMedals']].median())
        print('-' * 70)

        df['daysSpent'] = (pd.Timestamp.now() - pd.to_datetime(df.joined)).dt.days
        membership = df.sort_values(by='daysSpent', ascending=False)[['displayName',
                                                                      'tier',
                                                                      'daysSpent']]
        print('\n' + '=' * 35)
        print('Top 10 longest-time Kaggle members:')
        print('=' * 35 + '\n')
        print(membership.head(10))
        print('-' * 46)

        print('\n' + '=' * 46)
        print('Top 3 Kagglers by tier with the highest score:')
        print('=' * 46 + '\n')
        print(df[df.points.isin(df.groupby('tier').points.head(3).values.\
                     flatten())][['displayName', 'points', 'tier']])
        print('-' * 54 + '\n')
