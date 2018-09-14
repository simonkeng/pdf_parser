'''
Python 3.6 module for generating spaCy model 
from pickle file containing PDF data. 

Usage: 
import nlp

data = nlp.read('my-data.pkl')
doc = nlp.process(data)
'''

import spacy
import sys
import pickle

# word library to use
nlp = spacy.load('en_core_web_sm')

def read(pkl):
    with open(pkl, 'rb') as fp:
        data = pickle.load(fp)
    return data

def process(data):
    doc = nlp(data)
    return doc

def main(pkl):
    
    doc = process(read(pkl))

    # your analysis and parsing here...

    return doc


if __name__ == '__main__':
    main(sys.argv[1])

