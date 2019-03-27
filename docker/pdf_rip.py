'''
Python 2.7 command line tool for extracting
textual & numeric data from PDFs.

Usage: python pdf-rip.py document.pdf

'''

import textract
import pickle
import sys, os
import subprocess

def rip(fname):
    '''
    Extract data from the input file.

    input: file
    returns: unicode text from file
    '''

    data = unicode(textract.process(fname), 'utf-8')
    # data = textract.process(fname)
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

    write(rip(files), files)


if __name__ == '__main__':
    print os.getcwd()
    print subprocess.call(['ls'])
    main(sys.argv[1])

