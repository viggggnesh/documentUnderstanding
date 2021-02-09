import re
from os import listdir, path
import PyPDF2
import textract

class wranglePdf:
    def __init__(self, filePath):
        self.filePath = filePath


    def readPdf(self):
        
        self.fileObj = open(self.filePath, 'rb')
        self.fileReader = PyPDF2.PdfFileReader(self.fileObj)

    def printPdf(self):

        print(self.fileReader.numPages)
        readerObj = self.fileReader.getPage(0)
        print(readerObj.extractText())
        




if __name__ == "__main__":
    path = "C:/Users/gvign/Desktop/python-documentUnderstanfing/cover.pdf"

    wrangleObj = wranglePdf(path)
    wrangleObj.readPdf()
    wrangleObj.printPdf()

