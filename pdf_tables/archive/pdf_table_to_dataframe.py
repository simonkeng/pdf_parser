'''
Extract tables from PDFs and convert to pandas DataFrames 

Python 3.6 

Dependancies: 
- PyPDF2
- GhostScript
- tesseract 
- tabula-py

Contributor: Simon Keng
'''

import os, sys
import subprocess as sp
import argparse

from PyPDF2 import PdfFileWriter, PdfFileReader

from tabula

### Arg Parsing ###

parser = argparse.ArgumentParser()

parser.add_argument('--pdf', 
                    help='non-OCR input PDF file.')
parser.add_argument('--gs', 
                    help='Run GhostScript on each PDF to convert to TIFF.',
                    action="store_true")
parser.add_argument('--tess',
                    help='Run tesseract to OCR each TIFF image.',
                    action="store_true")

### Funcs ###

def chop(pdf):
    '''
    Chop up PDF by page
    '''
    input_pdf = PdfFileReader(open(pdf, 'rb'))

    for i in range(input_pdf.numPages):
        output = PdfFileWriter()
        output.addPage(input_pdf.getPage(i))
        with open(f'{i}.pdf', 'wb') as output_stream:
            output.write(output_stream)

def run_gs(pdf):
    '''
    Run simple, single arg shell script to convert PDF to TIFF
    '''
    shell_script = os.path.dirname(__file__) + '/pdf_to_tiff.sh'
    sp.call([shell_script, pdf])

def run_tesseract(tiff):
    '''
    '''
    outfile = tiff.split('.')[0] + '-ocr'
    sp.call(['tesseract', tiff, outfile, 'pdf'])


def build_pickle_file():

    for file in os.listdir(os.getcwd()):

        if file.endswith('-ocr.pdf'):
            
            
            # read new pickle file
            with open(new, 'rb') as rf:
                new_ch = pickle.load(rf)

            new_ch = new_ch

            # read old pickle file in the teams repo
            with open('tables.pkl', 'rb') as orf:
                old_ch = pickle.load(orf)

            old_ch = old_ch

            # concat old with new
            full_ch = old_ch + new_ch

            # overwrite the newly concat'd pickle file with the old one
            with open('tables.pkl', 'wb') as fwf:
                pickle.dump(full_ch, fwf)




#### Main ####

if __name__ == "__main__":
    
    args = parser.parse_args()

    # Chop up input PDF if "--pdf input.pdf"
    if args.pdf:
        print(f'Chopping up {args.pdf} by page..')
        chop(args.pdf)

    # Convert each PDF to TIFF if "--gs"
    if args.gs:
        print('Running GhostScript to generate TIFF images of each PDF file..')
        for pdf_file in os.listdir(os.getcwd()):
            if pdf_file != args.pdf:
                run_gs(pdf_file)

    # OCR each TIFF image if "--tess"
    if args.tess:
        print('Running tesseract OCR on each TIFF image..')
        for file in os.listdir(os.getcwd()):

            if file.endswith('.tif'):
                run_tesseract(file)
    


    

    





