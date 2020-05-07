from tkinter import *
from tkinter import filedialog

root = Tk()
root.title('Graphing Application')


root.filename = filedialog.askopenfilename(initialdir="/Desktop", title="Select a File", filetypes=(("xlsm files", "*.xlsm"), ("all files", "*.*")))
my_label = Label(root, text=root.filename)

root.mainloop()
