"""
Module containing model fitting code for a web application that implements a
text classification model.

When run as a module, this will load a csv dataset, train a classification
model, and then pickle the resulting model object to disk.
"""
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import BernoulliNB
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split

from sklearn.feature_extraction.text import CountVectorizer

class TextClassifier(object):
    """A text classifier model:
        - Vectorize the raw text into features.
        - Fit a naive bayes model to the resulting features.
    """

    def __init__(self):
        #self._vectorizer = TfidfVectorizer(stop_words='english')
        self._vectorizer = CountVectorizer()
        self._classifier = BernoulliNB()
        #self._classifier = MultinomialNB()

    def fit(self, X, y):
        """Fit a text classifier model.

        Parameters
        ----------
        X: A numpy array or list of text fragments, to be used as predictors.
        y: A numpy array or python list of labels, to be used as responses.

        Returns
        -------
        self: The fit model object.
        """
        # Code to fit the model.

        train_stuff = self._vectorizer.fit_transform(X,y)

        self._classifier.fit(train_stuff, y = y)


        return self

    def predict_proba(self, X):
        """Make probability predictions on new data."""

        stuff = self._vectorizer.transform(X)
        result = self._classifier.predict_proba(stuff)
        return result
        pass

    def predict(self, X):
        """Make predictions on new data."""

        stuff = self._vectorizer.transform(X)
        result = self._classifier.predict(stuff)
        return result
        pass

    def score(self, X, y):
        """Return a classification accuracy score on new data."""

        stuff = self._vectorizer.transform(X)
        result = self._classifier.score(stuff,y)

        return result
        pass



def get_data():
    """Load raw data from a file and return training data and responses.

    Parameters
    ----------
    filename: The path to a csv file containing the raw text data and response.

    Returns
    -------
    X: A numpy array containing the text fragments used for training.
    y: A numpy array containing labels, used for model response.
    """

    X = pd.read_csv('data/train.txt',header=None)
    y = pd.read_csv('data/labels.txt', header=None)

    return X[0],y
    pass


if __name__ == '__main__':
    X,y = get_data()

    tc = TextClassifier()

    X_train, X_test, y_train, y_test = train_test_split(X, y)
    tc.fit(X,y)

    print 'Score for corsss val on NB: ', tc.score(X_test,y_test)

    tc.fit(X, y)
    print ""
