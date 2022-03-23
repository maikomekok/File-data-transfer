from tkinter import *
from tkinter import filedialog
from fpdf import FPDF 
import os

root = Tk()
root.title('Converter')
root.geometry("250x100")


def open_file():
    #gilakis dacherisas gaaxsnevinebs fails
    root.filename = filedialog.askopenfilename(initialdir="", title='Select A File', filetypes=(('text files', '*.txt'),('all files', '*.*')))
    my_file = root.filename
    return my_file

def convert():
    my_file = open_file() #sheinaxavs gaxsnili failis saxels 
    # create object of FPDF class
    pdf = FPDF() 
    # create or add a page in pdf
    pdf.add_page() 
    # set font style and size for text 
    pdf.set_font("arial", size = 10) 
    # open test.txt file with read mode
    text_file = open("C:/Users/Lina/Desktop/project.txt", "r", encoding='UTF-8') 
    # use for loop to extract the text
    # from text_file and insert it into pdf cell 
    for text in text_file: 
        pdf.cell(200, 10, txt = text, ln=1,align='L') 
    # save the pdf with name .pdf 
    pdf.output("text_file_pdf.pdf")

    
    
    

my_btn = Button(root, text="Convert file", command=convert)
my_btn.grid(padx=80, pady=25)

root.mainloop()