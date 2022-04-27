from tkinter import *

import frac_dec
from units_ui import UnitsUI
from gears_ui import GearCalculator
from frac_dec_ui import FracDecUI
from reference import Table as rTable
from reference import works_cited

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


def hardware_select():
    """
    This function updates the variables sys_selection and type_selection for whenever the radio buttons for
    HARDWARE REFERENCE are selected. It also sets the value of the global variable option. This function is only to be
    used for hardware selection (type and system), and not for other aspects of the GUI.
    :return: None
    """
    sys_selection = str(var_1.get())
    type_selection = str(var_2.get())
    """
    Create a table object later on to show the table at the end of this function. From
    that file, the options are:
    
    1: metric screws, 2: standard screws 3: metric nuts 4: standard nuts
    """
    #variable to select the table
    #set it to 1 as default because: if one of the buttons is uninitiated in the code (due to the order of invoking)
    #for example, the first set of buttons is invoked and then the second. When the first set is invoked, the second
    #has no value, so it needs this default case
    option = 2

    # standard
    if sys_selection == "s":
        if type_selection == "sc":
            option = 2
        elif type_selection == "n":
            option = 4
    #metric
    elif sys_selection == "m":
        if type_selection == "sc":
            option = 1
        elif type_selection == "n":
            option = 3
    # insert the table
    table_frame = Frame(hardware_ref_frame, bg="#b59a19")
    table_frame.grid(row=1, column=0, columnspan=2, padx=5, pady=15)
    #This line creates a table object which is the reason the table shows up (because it is implemented in the
    # reference section
    table_to_show = rTable(option, table_frame, row_offset=1)


#picking the size (metric vs standard)
hardware_sys_frame = LabelFrame(hardware_ref_frame, text="System")
hardware_sys_frame.grid(column=0, row=0, pady=20)
#radio buttons to pick between metric and standard
var_1 = StringVar()  # For the system
var_2 = StringVar()  # For the type
standard_hardware = Radiobutton(hardware_sys_frame, text="Standard", variable=var_1, value="s", command=hardware_select)
standard_hardware.pack(side=LEFT)
#set the standard system on as default
standard_hardware.invoke()
metric_hardware = Radiobutton(hardware_sys_frame, text="Metric", variable=var_1, value="m", command=hardware_select)
metric_hardware.pack(side=LEFT)

#picking the type of hardware
hardware_type_frame = LabelFrame(hardware_ref_frame, text="Type")
hardware_type_frame.grid(column=1, row=0, pady=20)
#radio buttons to pick between nuts and machine screws
screws = Radiobutton(hardware_type_frame, text="Screws", variable=var_2, value="sc", command=hardware_select)
screws.pack(side=LEFT)
#set this as the default
screws.invoke()
nuts = Radiobutton(hardware_type_frame, text='Nuts', variable=var_2, value="n", command=hardware_select)
nuts.pack(side=LEFT)

#hardware works cited
works_cited_frame = LabelFrame(hardware_ref_frame, text="My References")
works_cited_frame.grid(row=10, column=0, columnspan=3, pady=20)
works_cited_button = Button(works_cited_frame, text="Click for Works Cited", command=lambda:
                            works_cited(works_cited_frame), width=30, bg="#a89a6a")
works_cited_button.pack(pady=10)

root.mainloop()
