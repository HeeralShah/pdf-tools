#!/usr/bin/python3

from PyPDF4 import PdfFileMerger

pdfs = ['hw1-ht2021.pdf', 'hw2-ht2021.pdf', 'hw3-ht2021.pdf', 'hw4-ht2021.pdf']

merger = PdfFileMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write("combined_hw.pdf")
merger.close()