#Oliver Hugh 4/1/2022
from tkinter import *

home = Tk()
home.title("Home")


def button_click(button_num: int):
    if button_num == 1:
        # gear calculator open up
        pass
    elif button_num == 2:
        # unit converter
        pass
    elif button_num == 3:
        # decimal/fraction converter
        pass
    elif button_num == 4:
        #hardware reference
        pass


instructions = Button(home, text="Please click on one of the options below to continue. Click here for references",
                      background='blue', fg='red', padx=340, pady=30)
instructions.pack()

gear_button = Button(home, text="Gear Calculator", padx=50, pady=20, activebackground='red', fg='blue', command=lambda: button_click(1))
unit_button = Button(home, text="Unit Converter", padx=50, pady=20, command=lambda: button_click(2))
dec_and_frac = Button(home, text="Decimal/Fraction Converter", padx=50, pady=20, command=lambda: button_click(3))
hardware_ref = Button(home, text="Hardware Sizes", padx=50, pady=20, command=lambda: button_click(4))


instructions.grid(row=0, column=0, columnspan=4)
gear_button.grid(row=1, column=0)
unit_button.grid(row=1, column=1)
dec_and_frac.grid(row=1, column=2)
hardware_ref.grid(row=1, column=3)


home.mainloop()
