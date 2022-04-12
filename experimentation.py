from tkinter import *

tkWindow = Tk()
tkWindow.geometry('400x150')
tkWindow.title('Button Background Example')

frame = LabelFrame(tkWindow, text="hello", padx=5, pady=5)
frame.grid(row=0, column=0, padx=5, pady=5)

button = Button(frame, text='Submit', activebackground='blue')
button.pack()


tkWindow.mainloop()

