from fpdf import FPDF 
import os
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



