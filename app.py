import textract
import spacy

# load spaCy model
nlp = spacy.load('en_core_web_sm')

# convert PDF into string and cast as unicode 
raw_data = unicode(textract.process('test_data.pdf'), 'utf-8')

# use model
doc = nlp(raw_data)

for ent in doc.ents:
    
    # if the entity label is geopolitical entity
    if ent.label_ == 'GPE':
        print ent.text
    

