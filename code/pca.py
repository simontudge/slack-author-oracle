"""
Takes the word matix and takes the n first principle components and saves the output.
"""

import pickle
import sys

from sklearn.decomposition import PCA


if __name__ == '__main__':

    n = int(sys.argv[1])

    # Load the sparse array into memory
    word_matrix = pickle.load(open('../features/word_matrix.pkl', 'rb'))

    # Intantiate the class and fit_transform the data
    pca = PCA(n_components=n)
    word_pcas = pca.fit_transform(word_matrix.toarray())

    # Dump back to another pickle file
    pickle.dump(word_pcas, open('../features/word_pcas.pkl', 'wb'))
