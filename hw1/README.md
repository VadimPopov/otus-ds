`gathering.py` is a script that scrapes the raw data off the [Kaggle](https://www.kaggle.com/) leaderboard, parses it into a pandas dataframe, and then shows some predefined user stats.

###### Dependencies: ######
* Python 3.5+
* pandas
* beautifulsoup4

The following commands are available:

* `python gathering.py gather` - gets raw data from Kaggle;
* `python gathering.py transform` - cleans the data and saves it to a dataframe;
* `python gathering.py stats` - calculates and displays user-defined statistics.
