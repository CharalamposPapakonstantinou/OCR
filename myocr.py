import pytesseract
from pdf2image import convert_from_path
import os
from tkinter import *
from tkinter import filedialog, ttk
from tkinter import messagebox


def ocr():
    global filename
    if 'filename' in globals():
        # Path of the pdf
        PDF_file = filename
        pages = convert_from_path(PDF_file, 500)
        savepath = os.path.splitext(filename)[0] + ' OCR' + '.txt'
        f = open(savepath, "a")
        for page in pages:
            text = str(((pytesseract.image_to_string(page))))
            text = text.replace('-\n', '')
            f.write(text)

        f.close()
        messagebox.showinfo("Done", "Result Saved at: \n" + os.path.splitext(filename)[0])

def open_file():
    global filename,N,win1,textpath
    filename = filedialog.askopenfilename(filetypes=(("Select PDF File", "*.pdf"),))

    if 'textpath' in globals():
        textpath.destroy()
    textpath = Label(win1, text=filename)
    textpath.pack(fill="both", expand=True,side=TOP)



win1 = Tk('App')

win1.geometry('500x200+00+00')
win1.resizable(width=True, height=True)
win1.title("Optical Character Recognition")
btn = Button(win1, text='Load PDF File',width=20,height=3, command=open_file)
btn.pack(side=TOP)

btn2 = Button(win1, text='Convert',width=20,height=3, command=ocr)
btn2.pack(side=BOTTOM)

win1.mainloop()

