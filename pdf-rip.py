import textract
import pickle
import sys

def rip(pdf):
    data = unicode(textract.process(pdf), 'utf-8')
    return data

def write(data):
    with open('pdf-data.pkl', 'wb') as fp:
        pickle.dump(data, fp)

def main(pdf):
    return write(rip(pdf))

if __name__ == '__main__':
    main(sys.argv[1])


