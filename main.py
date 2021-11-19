import pandas as pd;

RATINGS_DATA_FILE = './rating.csv'
MOVIES_DATA_FILE = './movie.csv'

# load the raw csv into a data_frame
df_ratings = pd.read_csv(RATINGS_DATA_FILE)

# drop the timestamp column since we dont need it now
df_ratings = df_ratings.drop(columns="timestamp")

# movies dataframe
df_movies = pd.read_csv(MOVIES_DATA_FILE)

# check we have 25M users' ratings
df_ratings.userId.count()