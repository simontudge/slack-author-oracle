"""
Takes the text of the messages and counts the inverse word frequency for all the
words that are commonly found in the messages (but excluding English stop words).
"""

import json
import pickle

from sklearn.feature_extraction.text import TfidfVectorizer

if __name__ == '__main__':

    # Simply get a list of all word strings in ourdata
    word_data = []
    for i,j in enumerate(json.load(open('../pre_processed/preprocessed.json','rt'))):
        if i%100 == 0:
            print(j['text'])
        word_data.append(j['text'])


    tf = TfidfVectorizer(stop_words='english')
    word_matrix = tf.fit_transform(word_data)

    pickle.dump(word_matrix, open('../features/word_matrix.pkl', 'wb'))
