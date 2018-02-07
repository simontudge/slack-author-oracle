"""
Performs step one of the process. Takes the raw files, and filters for the correct chanels
the users of interest and only those entries that are direct messages. It puts this all
into one output file. In addition it adds the channel to the json.
"""

import json
import os

from glob import glob
from itertools import chain

def include(element):
    """
    Returns true or false on whether to include a certain element
    """

    try:
        if element['user'] not in key_users:
            # The user should be one of our key users.
            return False
        elif element['type'] != 'message':
            return False
        elif 'subtype' in element.keys():
            return False
        else:
            return True
    except KeyError:
        return False

def file_interator():
    """
    Returns an interator over the files.
    The will be (chanel, file_name)
    """

    for c in chanels:
        file_list = iter(glob(os.path.join(raw_data_location, c, '*.json')))
        for file in file_list:
            yield (c, file)

first_write = True
def process_file(f, chanel, json_writer, text_writer):
    """
    Process the file. Write the json elements to
    the file, and all the raw text to another file.
    """

    with open(f, 'rt') as file:
        for element in json.load(file):
            if include(element):
                if not json_writer.first_write:
                    json_writer.write(',\n')
                else:
                    json_writer.first_write = False
                element['chanel'] = chanel
                json_writer.write(json.dumps(element))

                text_writer.write(element['text'])
                text_writer.write('\n')


def main():

    full_json_file = os.path.join(pre_processed_output, json_output)
    full_text_file = os.path.join(pre_processed_output, text_output)
    with open(full_json_file, 'wt') as j, open(full_text_file, 'wt') as f:

        j.write('[\n')
        j.first_write = True
        ## Begin an iterator over all files
        for chanel, file in file_interator():
            process_file(file, chanel, j, f)

        j.write('\n]')

chanels = ['brief_updates', 'discussion', 'general', 'help',
           'internal_discussions', 'knowledge_base', 'reference',
           'analysis', 'daily_huddle', 'hotbar', 'project_management', 'soton-office',
           'workshop_planning']

# For reference here is a list of users and their internal_discussions

# {'U04N457C0': 'Max Albert',
#  'U04NRTAEF': 'Elisabeth zu Erbach-Schoenberg',
#  'U04PJJX8K': 'Robin Wilson',
#  'U04SEMPC0': 'alansmith',
#  'U06ET559Q': 'Daniel Power',
#  'U06MX2MV1': 'Simon Tudge',
#  'U06P2RVD0': 'Miguel Gonzalez',
#  'U08GFA539': 'Linus Bengtsson',
#  'U09C7M7R9': 'jasondhilton',
#  'U0A9U1JB1': 'sam_guthrie',
#  'U0B3VH2KE': 'lenka',
#  'U0B4JQDJT': 'chrishughes',
#  'U0B4S0CTT': 'Chris Brooks',
#  'U0BFTU2G3': 'Heather Chamberlain',
#  'U0BFWG5N3': 'Jo Wilkin',
#  'U0BLS7ZGB': 'Jason Sadler',
#  'U0BRYDQ5T': 'Xin Lu',
#  'U0CBT2GTV': 'Luis Capelo',
#  'U0DRJMHBL': 'Jess Steele',
#  'U0FHGPCGK': 'Mathew Kiang',
#  'U0WTT399B': 'Laurent Oster',
#  'U1AUN84AX': 'Tomas Bird',
#  'U1BA2N7A7': 'evam.b.',
#  'U1FQYQ552': 'spadarian',
#  'U1GALLADP': 'rbergmair-urefraktor',
#  'U1HHT2CD7': 'Adam King',
#  'U1HQLDC56': 'Vincent Baumgartner',
#  'U1K3BSX1P': 'Guilherme Zagatti',
#  'U1MAT38UC': 'Annie Sheehan',
#  'U23NEDKPU': 'Priya Burci',
#  'U2MT46YF6': 'Jonathan Gray',
#  'U2WSAQSBG': 'Amy Ninneman',
#  'U2YDYMTPS': "Jamie O'Donnell",
#  'U2Z0GN2G6': 'Veronique Lefebvre',
#  'U2ZBEEHPF': 'Xavier Vollenweider',
#  'U2ZLL0WRF': 'Sarchil Qader',
#  'U30P8AYDR': 'Nick Ruktanonchai',
#  'U3LLS4Q4A': 'Richard Wood'}

key_users = ['U0B4S0CTT', 'U0CBT2GTV', 'U04N457C0', 'U06P2RVD0', 'U06MX2MV1']

file_location = os.path.dirname(__file__)
raw_data_location = os.path.join(file_location, '../raw_data')
pre_processed_output = os.path.join(file_location, '../pre_processed')
json_output = 'preprocessed.json'
text_output = 'all_text_preprocess.txt'

if __name__ == '__main__':

    main()
