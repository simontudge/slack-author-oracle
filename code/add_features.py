"""
Takes the data as created by pre_processed, loops through the file
and makes some features for each element of the list.

Saves this to csv.
"""

import os
import json
import time

import numpy as np

################# FEATURES #################

def is_chanel(element, chanel):
    """
    Returns true if the element is from the chanel.
    """

    return element['chanel'] == chanel

def is_edited(element):

    return 'edited' in element.keys()

def total_reactions(element):

    try:
        return len(element['reactions'])
    except KeyError:
        return 0

def total_words(element):

    return len(element['text'].split(' '))

def av_word_length(element):

    words = element['text'].split(' ')
    return np.mean([len(w) for w in words])

def is_weekend(element):

    g = time.gmtime(float(element['ts']))
    return g.tm_wday in [5, 6]

def is_between(element, h1, h2):
    """
    Returns true if the hour is between h1 and h2
    """

    g = time.gmtime(float(element['ts']))
    hour = g.tm_hour
    return hour >= h1 and hour < h2

def count_marks(element, mark):
    """
    Counts the appearances of the question mark in the
    text.
    """

    return element['text'].count(mark)

############ MAIN LOGIC ##################

def get_headers():
    """
    Returns a list of headers
    """

    headers = ['user']
    headers.extend(chanels)
    features = ['is_edited',
                'total_reactions',
                'total_words',
                'av_word_length',
                'is_weekend',
                'is_morning',
                'is_day',
                'is_evening',
                'is_night',
                'bangs',
                'commas',
                'colons',
                'semicolons',
                'fullstop',
                'question',
                'double_quote',
                'single_quote',
                'bracket']
    headers.extend(features)
    return headers

def main():
    
    full_file_in = os.path.join(pre_processed_output, json_output)
    full_file_out = os.path.join(out_location, out_name)
    with open(full_file_out, 'wt') as output:
        ## Write the headers here
        headers = get_headers()
        output.write(','.join(headers))
        output.write('\n')
        for element in json.load(open(full_file_in, 'rt')):

            features = [element['user']]
            for chanel in chanels:
                features.append(is_chanel(element, chanel))
            features.append(is_edited(element))
            features.append(total_reactions(element))
            features.append(total_words(element))
            features.append(av_word_length(element))
            features.append(is_weekend(element))

            # And do the day time things
            features.append(is_between(element, *morning))
            features.append(is_between(element, *day))
            features.append(is_between(element, *evening))
            features.append(is_between(element, *night))

            # Let's count punctuation marks as well
            marks = ['!', ',', ':', ';', '.', '?', '"', "'", '(']
            for mark in marks:
                features.append(count_marks(element, mark))

            output.write(','.join(map(str, features)))

            output.write('\n')

morning = (6,9)
day = (9, 18)
evening = (18, 23)
night = (0, 6)

file_location = os.path.dirname(__file__)
pre_processed_output = os.path.join(file_location, '../pre_processed')
out_location = os.path.join(file_location, '../features')
out_name = 'features.csv'
json_output = 'preprocessed.json'
from pre_process import chanels


if __name__ == '__main__':

    main()
