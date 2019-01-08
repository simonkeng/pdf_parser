'''
Python 2.7 command line tool for extracting
textual & numeric data from PDFs.

Usage: python pdf-rip.py document.pdf

'''

import textract
import pickle
import sys, os

def rip(fname):
    '''
    Extract data from the input file.

    input: file
    returns: unicode text from file
    '''

    data = unicode(textract.process(fname), 'utf-8')
    return data


def write(data, fname):
    '''
    Write input data to pickle file.

    input: data, filename
    returns: .pkl file to current working dir
    '''

    fname = fname.split('.')[0] + '.pkl'
    with open(fname, 'wb') as fp:
        pickle.dump(data, fp)


def main(files):

    # if a single PDF file
    if os.path.isfile(files):
        return write(rip(files), files)

    # if a folder containing a bunch of PDFs
    if os.path.isdir(files):
        for f in os.listdir(files):
            return write(rip(f), f) # currently not working..


if __name__ == '__main__':
    main(sys.argv[1])

