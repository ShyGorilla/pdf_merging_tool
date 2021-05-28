from PyPDF2 import PdfFileMerger
from os import listdir
import PyPDF2
import os
import signal

# Console colors
W = '\033[0m'  # white (normal)
R = '\033[31m'  # red
G = '\033[32m'  # green
O = '\033[33m'  # orange
B = '\033[34m'  # blue
P = '\033[35m'  # purple
C = '\033[36m'  # cyan
GR = '\033[37m'  # gray

def signal_handler(signal, frame):
    print(O + "\n\nCTRL + C" + W + " PRESSED")
    exit()

signal.signal(signal.SIGINT, signal_handler)

os.system('clear')
print(G +'''
$$$$$$$\  $$$$$$$\  $$$$$$$$\ 
$$  __$$\ $$  __$$\ $$  _____|
$$ |  $$ |$$ |  $$ |$$ |      
$$$$$$$  |$$ |  $$ |$$$$$\    
$$  ____/ $$ |  $$ |$$  __|   
$$ |      $$ |  $$ |$$ |      
$$ |      $$$$$$$  |$$ |      
\__|      \_______/ \__|      
            ''')
print( O + '    PDF MERGING TOOL' + W + '\n')

# creating an empty list
lst = []
readers = []

# number of elemetns as input
pdf = int(input("Enter number of pdf want to merge : "))

# iterating till the range
for i in range(0, pdf):
    ele1 = input("Enter file " + str(i+1) + " psth: ")
    ele = ele1.replace(" ", "")
    lst.append(ele) # adding the element

pdfWriter = PyPDF2.PdfFileWriter()

for i in range(len(lst)):

    try:
        pdfopen = open(lst[i], 'rb')
    except:
        print(R + '\nWrong file ' + O + str(i+1) + R + ' input.\n')
        exit()

    pdf1Reader = PyPDF2.PdfFileReader(pdfopen)

    for pageNum in range(pdf1Reader.numPages):
            pageObj = pdf1Reader.getPage(pageNum)
            pdfWriter.addPage(pageObj)

    # Now that you have copied all the pages in both the documents, write them into the a new document
    pdfOutputFile = open('MergedFiles.pdf', 'wb')
    pdfWriter.write(pdfOutputFile)
     
    # Close all the files - Created as well as opened
pdfOutputFile.close()
print(G + '\nSuccessfully merged the pdf files\n')

