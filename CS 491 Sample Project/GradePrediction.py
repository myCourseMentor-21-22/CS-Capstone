import os
from surprise import BaselineOnly
from surprise import Dataset
from surprise import Reader
from surprise.model_selection import cross_validate

file_path = os.path.expanduser('/Users/spencer/Documents/School/CS 491 Sample Project/grade.data')

reader = Reader(line_format='user item rating timestamp', sep='\t')

data = Dataset.load_from_file(file_path, reader=reader)

cross_validate(BaselineOnly(), data, verbose=True)