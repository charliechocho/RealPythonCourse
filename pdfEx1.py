import os
from PyPDF2 import PdfFileReader, PdfFileWriter

my_path = './book1-exercises/chp11/practice_files/'
out_path = './outputs'

inp_file = os.path.join(my_path, "Pride and Prejudice.pdf")
pdf_file = PdfFileReader(open(inp_file, 'rb'))
txt_file = PdfFileWriter()


#os.system('clear')
#print 'Number of pages: ', pdf_file.getNumPages()
#print 'Title: ', pdf_file.getDocumentInfo().title
#print 'Some document info: ', pdf_file.getDocumentInfo()
with open(os.path.join(out_path, 'pnp.txt'), 'w') as tmp_file:
    pg_count = pdf_file.getNumPages()
    for pages in range(2,6):
        cln_txt = pdf_file.getPage(pages).extractText()
        cln_txt = cln_txt.replace("  ", '\n')
        tmp_file.write(cln_txt)


#pdf_to_text = pdf_to_text.replace("  ", '\n')
#print pdf_to_text
