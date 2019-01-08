'''
Extract tables from PDFs and convert to pandas DataFrames 

Written in Python 3.6 

Dependancies: 
- PyPDF2
- ghostscript
- tesseract
- tabula-py

Contributor: Simon Keng

'''

import os, sys
import subprocess as sp
import argparse

from PyPDF2 import PdfFileWriter, PdfFileReader

import pandas as pd
import tabula

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
parser.add_argument('--csv',
                    help='Use tabula to generate DataFrames (saved as CSVs) from all "-ocr" PDFs in cwd.',
                    action="store_true")
parser.add_argument('--csv-no-ocr',
                    help='Use tabula to generate DataFrames (saved as CSVs) using all PDFs found in cwd.',
                    action="store_true")

### Funcs ###

def chop(pdf):
    '''
    Chop up PDF by page
    '''
    input_path = '../' + str(pdf)
    input_pdf = PdfFileReader(open(input_path, 'rb'))

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
    Run tesseract 
    '''
    outfile = tiff.split('.')[0] + '-ocr'
    sp.call(['tesseract', tiff, outfile, 'pdf'])

def pdf_to_csv():
    '''
    Run tabula to generate dataframes, saved as CSVs, 
    on all "-ocr" labelled PDFs in cwd. 
    '''

    for file in os.listdir(os.getcwd()):

        if file.endswith('-ocr.pdf'):

            print(f'On file: {file}')
            df = tabula.read_pdf(file, multiple_tables=True)

            outfile = file.split('-')[0]

            try:
                df.to_csv(f'{outfile}.csv', index=False)
            except AttributeError as err:
                for i, single_df in enumerate(df):
                    single_df.to_csv(f'{outfile}-{i}.csv', index=False)

def pdf_to_csv_no_ocr():
    '''
    Run tabula to generate dataframes, saved as CSVs,
    using all PDFs in cwd as input (not just the "-ocr" PDFs).
    '''

    for file in os.listdir(os.getcwd()):

        print(f'On file: {file}')
        df = tabula.read_pdf(file, multiple_tables=True)

        outfile = file.split('.')[0]

        try:
            df.to_csv(f'{outfile}.csv', index=False)
        except AttributeError as err:
            for i, single_df in enumerate(df):
                single_df.to_csv(f'{outfile}-{i}.csv', index=False)



#### Main ####

if __name__ == "__main__":
    
    args = parser.parse_args()

    # Chop up input PDFs if "--pdf input.pdf"
    # and store all processed data in "working/"
    if args.pdf:
        sp.call(['mkdir', 'working'])
        os.chdir('working/')
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
    
    # Run tabula to generate CSVs if "--csv"
    if args.csv:
        print('Running tabula..')
        pdf_to_csv()

    # Run tabula on ALL PDFs in cwd to generate CSVs if "--csv-no-ocr"
    if args.csv_no_ocr:
        print('Running tabula..')
        pdf_to_csv_no_ocr()
    
