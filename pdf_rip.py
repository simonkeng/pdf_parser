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

def write(data):
    with open('pdf-data.pkl', 'wb') as fp:
        pickle.dump(data, fp)

def main(pdfs):
    
    if len(pdfs) > 2:
        for pdf in pdfs[1:]:
            return write(rip(pdf))

    else:
        return write(rip(pdfs))

if __name__ == '__main__':
    if len(sys.argv) > 2:
        inp = sys.argv
    else:
        inp = sys.argv[1]

    main(inp)


