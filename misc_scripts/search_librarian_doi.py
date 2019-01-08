'''
Command line tool for searching DOI numbers in Librarian.

Usage: python search_librarian_doi.py filename.txt

Input: text file, looking like this
10.1021/jm048972v
10.1021/jm0495778
10.1021/jm030650o
10.1021/jm0304358
10.1021/jm0005353

Output: printed to STDOUT
---------------------------------------------------
10.1021/jm048972v was not found in Librarian...
---------------------------------------------------
10.1021/jm0495778 was found! Librarian ID: 198
Fragment-based lead discovery using X-ray crystallography.

---------------------------------------------------
10.1021/jm030650o was found! Librarian ID: 2593
Validation of automated docking programs for docking and database screening against RNA drug targets.

---------------------------------------------------
10.1021/jm0304358 was found! Librarian ID: 1221
General model for estimation of the inhibition of protein kinases using Monte Carlo simulations.

---------------------------------------------------
10.1021/jm0005353 was not found in Librarian...
---------------------------------------------------

Questions?

Simon Keng
simon.keng@schrodinger.com

'''

import requests
import sys

API_URL = 'https://lucy.schrodinger.com/librarian/servlet.php'

def get_it():
    f = open(sys.argv[1], 'r')
    t = f.read()
    l = t.split('\n')
    print 'Found ' + str(len(l)) + ' DOI numbers in ' + str(sys.argv[1])
    decide = raw_input('Continue? (y/n): ')
    if decide == 'y':
        for i in range(0, (len(l) - 1)):
            payload = {'doi': l[i]}
            response = requests.post(API_URL, payload)
            text = str(response.text.encode('utf8'))
            if (text == ''):
                print str(l[i]) + ' was not found in Librarian...'
            if (text != ''):
                print str(l[i]) + ' was found! Librarian ID: ' + text
            print '---------------------------------------------------'
    elif decide == 'n':
        sys.exit()
    else:
        print "Only options are 'y' for YES and 'n' for NO."
    f.close()

if __name__ == '__main__':
    get_it()
