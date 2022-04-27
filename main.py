from tkinter import *
from units_ui import UnitsUI
from gears_ui import GearCalculator
from frac_dec_ui import FracDecUI
from reference import ReferenceUI

root = Tk()

root.title("Designer's Reference")
#root.geometry('1400x400')

#Instruction Frame
instruction_frame = LabelFrame(master=root, text="Instructions", bg='#c9ad20')
instruction_frame.grid(row=0, column=0, padx=5, pady=5, columnspan=4)
instruction_text = "Hello! This is an application meant as a quick reference to designers working with CAD.\n" \
                   "This is my final project for EECE 2140: Computing Fundamentals. Simply select between the\n " \
                   "different options for each individual calculator/convertor and input data for results! -Oliver Hugh"
instruction_label = Label(master=instruction_frame, text=instruction_text, bg='#c9ad20', width=130)
instruction_label.grid(row=0, column=0, columnspan=4, pady=2)


#The Gear Calculator Frame
gear_frame = LabelFrame(master=root, text="Gear Calculator", bg='#c98a00')
gear_frame.grid(row=1, column=0, padx=5, pady=5)
gear_instructions = Label(gear_frame, text="Enter all information below \nto calculate center distance.", bg='#c98a00')
gear_instructions.grid(column=0, row=0, padx=5, pady=5)
gear_calc = GearCalculator(gear_frame)

#The Unit Calculator Frame
unit_frame = LabelFrame(master=root, text="Unit Convertor", bg='#7a6d17')
unit_frame.grid(row=1, column=1, padx=5, pady=5)
unit_calc = UnitsUI(unit_frame)


#The Decimal/Fraction Convertor
dec_frac_frame = LabelFrame(root, text="Decimal/Fraction Convertor", bg='#e09758')
dec_frac_frame.grid(row=1, column=2, padx=5, pady=4)
dec_frac_calc = FracDecUI(dec_frac_frame)


#Hardware reference frame
hardware_ref_frame = LabelFrame(root, text="Hardware Reference", bg='#b8341a')
hardware_ref_frame.grid(row=1, column=3, padx=5, pady=5)
ref_display = ReferenceUI(hardware_ref_frame)


root.mainloop()
