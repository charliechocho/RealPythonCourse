import os
from PyPDF2 import PdfFileReader

my_path = './book1-exercises/chp11/practice_files/'

inp_file = os.path.join(my_path, "Pride and Prejudice.pdf")
pdf_file = PdfFileReader(open(inp_file, 'rb'))

os.system('clear')
print 'Number of pages: ', pdf_file.getNumPages()
print 'Title: ', pdf_file.getDocumentInfo().title
