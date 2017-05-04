##1) Complete this function that will give the number of jobs on indeed from a search result.

import requests
from bs4 import BeautifulSoup

def number_of_jobs(query):
    '''
    INPUT: string
    OUTPUT: int

    Return the number of jobs on the indeed.com for the search query.
    '''

    url = "http://www.indeed.com/jobs?q=%s" % query.replace(' ', '+')
    content = requests.get(url).content
    soup = BeautifulSoup(content)

    count = soup.find(id ="searchCount")

    return count.split('of')[-1]
    ### YOUR CODE HERE ###
For example:

In [62]: number_of_jobs('data scientist')
Out[62]: 13601  # Value will not necessarily be the same


##2) Say I am detecting fraud. If I identify a user as fraud, I will call them to confirm their identity. This costs $10. Catching fraud saves us $100. What does my cost benefit matrix look like?

Predicted fraud and was fraud (100 savings - 10 for call)
predicted fraud and not ( -10 for call)

as we are not given any cost for not catching fraud below is the cost benefit matrix


        Model 1:
                Actual
                Y    N
              -----------
           Y | 90 | -10 |
Predicted     -----------
           N |  0 |  0  |
              -----------


##3) We've built two different models for fraud which result in the following two confusion matrices.

        Model 1:                          Model 2:
                Actual                            Actual
                Y    N                            Y    N
              -----------                       -----------
           Y | 150 | 150 |                   Y | 200 | 500 |
Predicted     -----------         Predicted     -----------
           N |  50 | 650 |                   N |   0 | 300 |
              -----------                       -----------
Using your cost-benefit matrix from above, which model gives us the most profit?


        Model 1:                          Model 2:
                Actual                            Actual
                Y    N                            Y    N
              -----------                     -----------
           Y | 13500 | -1500 |           Y | 18000 | -5000 |
Predicted     ---------------         Pr    ----------------
           N |  0   |   0   |             N |   0  |    0  |
              -----------

Total model 1 = 12000
total model 2 = 12000

However one would assume that not catching fraud would be costly so model 2 would be the better option as it minimizes false negitives.

##4) Consider a corpus made up of the following four documents:

# Doc 1: Dogs like dogs more than cats.
# Doc 2: The dog chased the bicycle.
# Doc 3: The cat rode in the bicycle basket.
# Doc 4: I have a fast bicycle.
# We assume that we are lowercasing everything, lemmatizing, and removing stop words and punctuation. These are the features you should have:
#
# dog, like, cat, chase, bicycle, ride, basket, fast
# 3      1    2     1       3       1     1        1
# For these questions, don't worry about normalizing the results.
#
# What is the term frequency vector for Document 1?

dog:2/4 like:1/4 cat: 1/4



What is the document frequency vector for all the words in the corpus?


##5)  Given the same documents, use python to build the tf-idf vectors and calculate the cosine similarity of each document with each other document. For your convenience, here's the data in a python list:

documents = ["Dogs like dogs more than cats.",
             "The dog chased the bicycle.",
             "The cat rode in the bicycle basket.",
             "I have a fast bicycle."]
Which two documents are the most similar?

Please include your code in your solution.

## 6) What is wrong with this approach to building my feature matrix?

We assume that documents is a list of the text of emails, each as a string. y is an array of 0, 1 labels of whether or not the email is spam.

vect = TfidfVectorizer(stop_words='english')
X = vect.fit_transform(documents)
X_train, X_test, y_train, y_test = train_test_split(X, y)
log_reg = LogisticRegression()
log_reg.fit(X_train, y_train)
print "Accuracy on test set:", log_reg.score(X_test, y_test)
Redo the code to fix the issue.

## 7) Why do we need to do Laplace Smoothing in Naive Bayes?
  This allows us to deal with zero counts (words woht zero count or new words not in current classes/ training set)




## 8) Suppose N = 100 represents a dense sample for a three dimensional feature space.
#To achieve same density in an eight dimensional feature space, how many points would we need?

the need is exponental so one way to look at it is we need the density a dimension x to be initial size at dimension 2 ^(x-1)

so N at demnsion 2 is 10.  so it would go from 100 at d3 to 10^8 at d8 or we need 100000000 points.


## 9) The first step in the K-means algorithm involves randomly assigning data points to clusters, and as such, only finds local minimums. How do we typically deal with this?

We recursavely recalculate the cluster point and points assignment.


## 10) Describe the process of varying K in K-means. Contrast this with the process of varying K in the hierarchical clustering setting.
