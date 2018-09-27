'''
Python 2.7 command line tool, intended for execution in Docker container

Usage: python pdf-rip.py some-pdf-file.pdf
'''

import textract
import pickle
import sys, os

def rip(pdf):

    data = unicode(textract.process(pdf), 'utf-8')
    return data

def write(data, fname):
    fname = fname.split('.')[0] + '.pkl'
    with open(fname, 'wb') as fp:
        pickle.dump(data, fp)

def main(pdfs):

    # if a single PDF file 
    if os.path.isfile(pdfs):
        return write(rip(pdfs), pdfs)
    
    # if a folder containing a bunch of PDFs
    if os.path.isdir(pdfs):
        for f in os.listdir(pdfs):
            return write(rip(f), f) # currently not working.. 

if __name__ == '__main__':
    main(sys.argv[1])

