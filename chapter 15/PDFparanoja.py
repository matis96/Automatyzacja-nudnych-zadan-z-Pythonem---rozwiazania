#! python3
import sys
import os
import PyPDF2
from pathlib import Path
path = Path.cwd()
password = sys.argv[0]      # use bat file
for folder, subfolders, filenames in os.walk(path):
    for fileName in filenames:
        if fileName.endswith('.pdf'):
            oldPath = '\\'.join([folder, fileName])
            pdfFileObj = open(oldPath, 'rb')
            pdfReader = PyPDF2.PdfReader(pdfFileObj)
            newPath = oldPath[:-4]+'_encrypted.pdf'
            if pdfReader.is_encrypted is False:
                pdfWriter = PyPDF2.PdfWriter()
                for pageNum in range(len(pdfReader.pages)):
                    pageObj = pdfReader.pages[pageNum]
                    pdfWriter.add_page(pageObj)
                pdfOutputFile = open(newPath, 'wb')
                pdfWriter.encrypt(password)
                pdfWriter.write(pdfOutputFile)
                pdfOutputFile.close()
            pdfFileObj.close()

            # odszyfrowanie i odczytanie kopii
            pdfTrial = open(newPath, 'rb')
            pdfReader = PyPDF2.PdfReader(pdfTrial)
            if pdfReader.decrypt(password):
                pdfTrial.close()
                os.remove(oldPath)


