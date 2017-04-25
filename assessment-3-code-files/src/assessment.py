'''
* Fill each each function stub according to the docstring.
* To run the unit tests: Make sure you are in the root dir(assessment-3)
  Then run the tests with this command: "make test"
'''

from numpy.random import beta as beta_dist
import numpy as np
import scipy.stats as st
from sklearn.linear_model import LinearRegression
import pandas as pd
import random


# Probability

def roll_the_dice():
    '''
    INPUT: None
    OUTPUT: FLOAT

    Two unbiased dice are thrown once and the total score is observed. Use a
    simulation to find the estimated probability that the total score is even
    or greater than 7.
    '''
    win=0.0

    rep= 1000
    for i in xrange(rep):
        tot= np.random.randint(1,6)+np.random.randint(1,6)

        if tot % 2 == 0 or tot > 7:
            win+=1

    return win/(float(rep))


# A/B Testing

def calculate_clickthrough_prob(clicks_A, views_A, clicks_B, views_B):
    '''
    INPUT: INT, INT, INT, INT
    OUTPUT: FLOAT

    Calculate and return an estimated probability that SiteA performs better
    (has a higher click-through rate) than SiteB.

    Hint: Use Bayesian A/B Testing (multi-armed-bandit repo)
    '''

    samp = 10000
    Aa = clicks_A + 1
    Ab = clicks_B + 1
    Ba = views_A - clicks_A + 1
    Bb = views_B - clicks_B + 1

    A_prob = beta_dist(Aa, Ba, samp)
    B_prob = beta_dist(Ab, Bb, samp)

    return np.sum(A_prob > B_prob)/float(samp)


# Statistics

def calculate_t_test(sample1, sample2, type_I_error_rate):
    '''
    INPUT: NUMPY ARRAY, NUMPY ARRAY
    OUTPUT: FLOAT, BOOLEAN

    You are asked to evaluate whether the two samples come from a population
    with the same population mean.
    Return a tuple containing the p-value for the pair of samples and True or
    False depending if the p-value is considered significant at the provided Type I Error Rate.
    '''
    test = st.ttest_ind(sample1,sample2)
    return test[1],test[1]<type_I_error_rate
    pass


# Pandas and Numpy

def pandas_query(df):
    '''
    INPUT: DATAFRAME
    OUTPUT: DATAFRAME

    Given a DataFrame containing university data with these columns:
        name, address, Website, Type, Size

    Return the DataFrame containing the average size of the university for each
    type ordered by size in ascending order.
    '''
    df1 = df.groupby(by='Type')['Size'].mean()
    df1.sort()
    return df1


def df_to_numpy(df, y_column):
    '''
    INPUT: DATAFRAME, STRING
    OUTPUT: 2 DIMENSIONAL NUMPY ARRAY, NUMPY ARRAY

    Make the column named y_column into a numpy array (y) and make the rest of
    the DataFrame into a 2 dimensional numpy array (X). Return (X, y).

    E.g.
                a  b  c
        df = 0  1  3  5
             1  2  4  6
        y_column = 'c'

        output: [[1, 3], [2, 4]],   [5, 6]
    '''
    ## per answers need to copy
    ## dumb = df.copy()
    y = df.pop(y_column)
    return np.array(df),np.array(y)


def only_positive(arr):
    '''
    INPUT: 2 DIMENSIONAL NUMPY ARRAY
    OUTPUT: 2 DIMENSIONAL NUMPY ARRAY

    Return a numpy array containing only the rows from arr where all the values
    are positive.

    E.g.  np.array([[1, -1, 2], [3, 4, 2], [-8, 4, -4]])
              ->  np.array([[3, 4, 2]])

    DO NOT use a for loop.
    '''
    return arr[arr.min(axis=1)>=0]
    pass


def add_column(arr, col):
    '''
    INPUT: 2 DIMENSIONAL NUMPY ARRAY, NUMPY ARRAY
    OUTPUT: 2 DIMENSIONAL NUMPY ARRAY

    Return a numpy array containing arr with col added as a final column. You
    can assume that the number of rows in arr is the same as the length of col.

    E.g.  [[1, 2], [3, 4]], [5, 6]  ->  [[1, 2, 5], [3, 4, 6]]
    '''

    return np.concatenate((arr, col.reshape((-1,1))), axis = 1)
    pass


def size_of_multiply(A, B):
    '''
    INPUT: 2 DIMENSIONAL NUMPY ARRAY, 2 DIMENSIONAL NUMPY ARRAY
    OUTPUT: TUPLE

    If matrices A (dimensions m x n) and B (dimensions p x q) can be
    multiplied, return the shape of the result of multiplying them. Use the
    shape function. Do not actually multiply the matrices, just return the
    shape.

    If A and B cannot be multiplied, return None.
    '''
    '''In brodcasting in 2 dmentions the important thing is if the columns for A matches the rows for B '''

    if A.shape[1] == B.shape[0]:
        return A.shape[0], B.shape[1]
    return None
# Linear Regression

def linear_regression(X_train, y_train, X_test, y_test):
    '''
    INPUT: 2 DIMENSIONAL NUMPY ARRAY, NUMPY ARRAY
    OUTPUT: TUPLE OF FLOATS, FLOAT

    Use the sklearn LinearRegression to find the best fit line for X_train and
    y_train. Calculate the R^2 value for X_test and y_test.

    Return a tuple of the coefficients and the R^2 value. Should be in this form:
    (12.3, 9.5), 0.567
    '''
    model = LinearRegression(fit_intercept=True, normalize=False)
    model.fit(X_train, y_train)

    return (model.coef_,model.score(X_test, y_test))
    pass

# SQL

def sql_query():
    '''
    INPUT: None
    OUTPUT: STRING

    sqlite> PRAGMA table_info(universities);
    0,name,string,0,,0
    1,address,string,0,,0
    2,url,string,0,,0
    3,type,string,0,,0
    4,size,int,0,,0

    Return a SQL query that gives the average size of each type of university
    in ascending order.
    Columns should be: type, avg_size
    '''
    return '''SELECT type, AVG(size) as s from universities GROUP BY type ORDER BY s;'''
    # Your code should look like this:
    # return '''SELECT * FROM universities;'''
    pass
