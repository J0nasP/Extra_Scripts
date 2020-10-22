import tkinter, os
from tkinter import filedialog, simpledialog
from PyPDF2 import PdfFileReader, PdfFileWriter, PdfFileMerger
from pathlib import *






def pdf_splitter():
    
    file_name = filedialog.askopenfilename(title = "choose a file",
                                     initialdir = '\\' )

    the_file_name = ''.join(file_name)
    pdf = PdfFileReader(the_file_name)
    fname = os.path.splitext(os.path.basename(the_file_name))[0]

    dest_folder = filedialog.askdirectory(title = "choose the output folder",
                                            initialdir = '\\')
    out_folder = ''.join(dest_folder)


    for page in range(pdf.getNumPages()):
        pdfFileWriter = PdfFileWriter()
        pdfFileWriter.addPage(pdf.getPage(page))

        output_file = os.path.join(out_folder, '{} page {}.pdf'.format(
            fname, page+1))
        with open(output_file, 'wb') as out:
            pdfFileWriter.write(out)


def merger():
    dir_now = filedialog.askdirectory(title = 'where is it?',
                                        initialdir = "\\")

    userpdflocation = dir_now
    os.chdir(userpdflocation)


    what_name = simpledialog.askstring(title = 'What?' , prompt = 'Name the file',)
    userfilename = what_name

    pdf2merge = []
    for filename in os.listdir('.'):
        if filename.endswith('.pdf'):
            pdf2merge.append(filename)

    pdfWriter = PdfFileWriter()


    for filename in pdf2merge:
        pdffileObj = open (filename, 'rb')
        pdfReader = PdfFileReader(pdffileObj)
        
        for pageNum in range(pdfReader.numPages):
            pageObj = pdfReader.getPage(pageNum)
            pdfWriter.addPage(pageObj)
        
    pdfOutput = open(userfilename + '.pdf', 'wb')
    pdfWriter.write(pdfOutput)
    pdfOutput.close()
