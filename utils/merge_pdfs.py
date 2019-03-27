from PyPDF2 import PdfFileMerger
import sys
import os

pdfs = os.listdir(os.getcwd())

merger = PdfFileMerger()


for pdf in pdfs:
    merger.append(open(pdf, 'rb'))

with open('merged.pdf', 'wb') as fout:
    merger.write(fout)
