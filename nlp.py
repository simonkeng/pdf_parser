import spacy
import sys
import pickle

# model to use
nlp = spacy.load('en_core_web_sm')

def read(pkl):
    with open(pkl, 'rb') as fp:
        data = pickle.load(fp)
    return data

def apply_model(data):
    doc = nlp(data)
    return doc

def main(pkl):
    
    doc = apply_model(read(pkl))

    # your analysis and parsing here...

    for token in doc:

        # IC50 
        if token.shape_ == 'XXdd':
            
            print('TOKEN', token.text)
            print('SENTENCE', token.sent)


if __name__ == '__main__':
    main(sys.argv[1])

