from tkinter import *
from tkinter import filedialog

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
<<<<<<< HEAD
    
=======
    print(my_file)
>>>>>>> 684250e12796893e5d03c5213eb5f934ae890e6b

    
    
    

my_btn = Button(root, text="Convert file", command=convert)
my_btn.grid(padx=80, pady=25)

root.mainloop()