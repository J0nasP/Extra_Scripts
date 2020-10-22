import glob, win32com.client, docx, os
from docxcompose.composer import Composer
from docx import Document
from tkinter import filedialog
from docx2pdf import convert




def pdfToWord():
    file_directory = filedialog.askdirectory(title = "Select folder",
                                          initialdir = "/")

    word = win32com.client.Dispatch("Word.Application")
    word.visible = 0
    

    pdfs_path = file_directory # folder where the .pdf files are stored
    for i, doc in enumerate(glob.iglob(pdfs_path+"*.pdf")):
        print(doc)
        filename = doc.split('\\')[-1]
        input_file = os.path.abspath(doc)
        print(input_file)
        wb = word.Documents.Open(input_file)
        output_file = os.path.abspath(filename[0:-4]+ "{}.docx".format(i))
        print("outputfile\n",output_file)
        wb.SaveAs2(output_file, FileFormat=16) # file format for docx
        print("success...")
        wb.Close()

    word.Quit()


def wordTogetherForEver():
    file_directory = filedialog.askdirectory(title = "Select folder",
                                              initialdir = "/")

    new_file_name = filedialog.asksaveasfilename(filetype = [('.docx', 'word')],
                                                    title = 'Write the new filename')
    master = docx.Document(docx = None)
    input_folder = file_directory
    folder_directory = os.listdir(input_folder)
    composer = Composer(master)
    
    for filename in folder_directory:
        if filename.endswith('.docx'):
            composer.append(Document(filename))

    composer.save( new_file_name + '.docx' )


def backTopPfAgain():
    
    file_directory = filedialog.askdirectory(title = "Select the input folder",
                                            initialdir = "/")
    output_path = filedialog.askdirectory(title = "Select select the output folder",
                                            initialdir = "/")

    input_folder = file_directory
    output_folder = output_path
    folder_directory = os.listdir(input_folder)

    for filename in folder_directory:
        if filename.endswith('.docx'):
            convert(filename, output_folder)
            