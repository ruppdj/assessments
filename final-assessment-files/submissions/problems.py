'''
Section 1 of Final Assessment.
You can run tests for this section by running "make test" from the root repo(final-assessment)
'''

import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
import requests


def column_averages(filename):
    '''
    INPUT: string
    OUTPUT: dictionary (string => float)

    Take the name of a csv file. The first line of the file is the column names.
    All of the column values are numerical. Return a dictionary containing the
    average value for each column.
    '''

    df = pd.read_csv(filename)
    cols = df.columns.values
    avg = df.mean(axis=0)
    d = dictionary(float)
    for key,val in zip(cols,avg):
        d[key]=val
    return d
    pass


def filter_by_class(X, y, label):
    '''
    INPUT: 2 dimensional numpy array, numpy array, object
    OUTPUT: 2 dimensional numpy array

    Return the rows from X whose corresponding label from y is the given label.
    '''

    return np.array(X[y==label])


def etsy_query(query):
    '''
    INPUT: string
    OUTPUT: list of strings

    Take a query and return a list of all of the etsy usernames who have a
    result on the first page of that query result.
    '''
    

    pass
