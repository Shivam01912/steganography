from Tkinter import *
from tkFileDialog import askopenfilename
import tkMessageBox

top = Tk()
files=""
def browsing():
	filename=askopenfilename()
   	pathlabel.config(text=filename)
   	global files
   	files=filename

def conversion():
	if files=="" :
		tkMessageBox.showinfo( "WARNING", "Please select a file...!!")
	else:
		if len(str(E1.get()))!=16:
			tkMessageBox.showinfo( "WARNING", "Please enter the a character long key")
		elif str(E2.get())=="":
			tkMessageBox.showinfo( "WARNING", "Please enter your message")

	

image_browse = Button(top, text="Browse", command=browsing)
image_browse.grid(row=0, column=2)

pathlabel = Label(top)
pathlabel.grid(row=0,column=0)

L1 = Label(top, text="Encryption key (16 characters)")
L1.grid( row=1)
E1 = Entry(top, bd =5)	
E1.insert(END, 'This is a key123')
E1.grid( row=1, column=2)

L2 = Label(top, text="Message")
L2.grid( row=2, column=0)
E2 = Text(top, bd =5, height=7, width=30)
#E2.insert(INSERT, 'This is message1')
E2.grid(row=2,column=2)

B = Button(top, text ="Encrypt", command = conversion)
B.grid(row=5)

top.mainloop()