# importing required modules
import PyPDF2

def parser(data):
    # creating a pdf file object
    pdfFileObj = data

    # creating a pdf reader object
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

    # creating a page object
    pageObj = pdfReader.getPage(0)

    # extracting text from page
    test = pageObj.extractText()

    # closing the pdf file object
    pdfFileObj.close()

    return test

    