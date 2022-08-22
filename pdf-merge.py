#!/usr/bin/python3

from PyPDF4 import PdfFileMerger
from tkinter  import Tk
from tkinter import filedialog
from tkinter.filedialog import askopenfilename, askdirectory

Tk().withdraw()

print("choose two or more files")

filename = askopenfilename()
filename2 = askopenfilename()

pdfs = [filename, filename2]
# print(pdfs)

answer = None
while answer not in ("y", "n"):
    answer = input("do you wish to add more files? choose y/n: ")
    print(answer)
    if answer == "y":
        extra_file= askopenfilename()
        pdfs.append(extra_file)
        answer = None
    elif answer == "n":
        exit
    else:
        print("please enter y/n")
    


merger = PdfFileMerger()


### add try catch for empty list
for pdf in pdfs:
    merger.append(pdf)


location = askdirectory(title="Save merged pdf")
filename_merged = input("please enter a valid filename: ") + ".pdf"

merger.write(location + "/" + filename_merged)

merger.close()