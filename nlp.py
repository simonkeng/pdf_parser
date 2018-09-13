import spacy
import sys
import pickle

# word library to use
nlp = spacy.load('en_core_web_sm')

def read(pkl):
    with open(pkl, 'rb') as fp:
        data = pickle.load(fp)
    data = data.split(' ')
    
    if '\n' in data:
        data.remove('\n')

    print(data)


    return data

def process(data):
    doc = nlp(data)
    return doc

def main(pkl):
    
    doc = process(read(pkl))

    # your analysis and parsing here...

    for token in doc:

        # IC50 
        if token.shape_ == 'XXdd':
            
            print('TOKEN', token.text)
            print('SENTENCE', token.sent)


if __name__ == '__main__':
    # main(sys.argv[1])
    read(sys.argv[1])
