"""
This is the file that takes the csv and performs some simple
out of the box machine learning techniques to identify who wrote
the message.
"""

import pickle

import pandas as pd
import numpy as np

from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix

if __name__ == '__main__':

    # Load the csv
    df = pd.read_csv('../features/features.csv')

    # Split the csv into the list of features and labels
    labels = np.array(df['user'])
    features_meta = np.array(df[df.columns[1:]])

    # Additional features are the word frequency matrices
    # They should be in the same order as the other features
    # so we simply need to load and append.
    features_word = pickle.load(open('../features/word_pcas.pkl', 'rb'))

    features = np.concatenate([features_meta, features_word], axis=1)
    # Split into training and testing
    features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.1)

    # Train the algorithm
    clf = RandomForestClassifier(n_estimators=25, min_samples_split=10)
    clf.fit(features_train, labels_train)

    # Print the score of the algorithm
    score = clf.score(features_test, labels_test)
    print('Score: {}'.format(score))

    print('Confusion Matrix:')
    print(confusion_matrix(clf.predict(features_test), labels_test))
