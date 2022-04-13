from tkinter import *

import frac_dec
import units
import gears
from reference import Table as rTable
from reference import works_cited

root = Tk()

root.title("Designer's Reference")
#root.geometry('1400x400')

#Instruction Frame
instruction_frame = LabelFrame(master=root, text="Instructions", bg='#c9ad20')
instruction_frame.grid(row=0, column=0, padx=5, pady=5, columnspan=4)
instruction_text = """Hello! This is an application meant as a quick reference to designers working with CAD. 
This is my final project for EECE 2140: Computing Fundamentals. Simply select between the 
different options for each individual calculator/convertor and input data for results! -Oliver Hugh"""
instruction_label = Label(master=instruction_frame, text=instruction_text, bg='#c9ad20', width=90)
instruction_label.grid(row=0, column=0)


#The Gear Calculator Frame
gear_frame = LabelFrame(master=root, text="Gear Calculator", bg='#c98a00')
gear_frame.grid(row=1, column=0, padx=5, pady=5)
gear_instructions = Label(gear_frame, text="Enter all information below \nto calculate center distance.", bg='#c98a00')
gear_instructions.grid(column=0, row=0, padx=5)

#entry for num teeth in gear 1
gear_1_frame = LabelFrame(gear_frame, text="Gear 1 # of Teeth:", bg='#c98a00')
gear_1_frame.grid(column=0, row=1, pady=5, padx=2)
gear_1_entry = Entry(gear_1_frame, width=15, bg='#f7e6d0')
gear_1_entry.pack()
#entry for num teeth in gear 2
gear_2_frame = LabelFrame(gear_frame, text="Gear 2 # of Teeth:", bg='#c98a00')
gear_2_frame.grid(column=0, row=2, pady=5, padx=2)
gear_2_entry = Entry(gear_2_frame, width=15, bg='#f7e6d0')
gear_2_entry.pack()
#Drop-down for dp
dp_frame = LabelFrame(gear_frame, text="Diametral Pitch", bg='#f7e6d0')
dp_frame.grid(column=0, row=3, pady=5, padx=2)
#list of standard diametral pitches
dp_list = [12, 16, 18, 20, 24, 32, 48]
dp = IntVar()
dp_drop = OptionMenu(dp_frame, dp, *dp_list)
dp_drop.pack()
dp.set(dp_list[0])
#include a blank label to increase the size of the frame
spacer_label = Label(dp_frame, width=15, bg='#f7e6d0')
spacer_label.pack()
gear_result_frame = LabelFrame(gear_frame, text="Center to Center distance:", bg='#f7e6d0')
gear_result_frame.grid(row=5, column=0, pady=5)
gear_result = Entry(gear_result_frame, width=15, bg='#f7e6d0')
gear_result.pack()


def gear_calculation(gear_dp):
    """
    This function calculates the center to center distance of 2 gears using functions from the
    gears file and inserts the result inside the gear_result entry
    :param gear_dp: the diametral pitch of the gears
    :return: None
    """
    teeth_1 = int(gear_1_entry.get())
    teeth_2 = int(gear_2_entry.get())

    if type(teeth_1) is int and type(teeth_2) is int and teeth_1 is not None and teeth_2 is not None:
        #now use functions from the gears file to calculate the center to center distance
        gear_answer = gears.calculate_center(teeth_1, teeth_2, gear_dp)
        gear_result.delete(0, END)
        gear_result.insert(END, str(gear_answer) + " in")


#button to calculate. This is created after the entry (even though it is above it) because its command
#function references the gear_result entry
gear_button = Button(gear_frame, width=15, text="Calculate Result", command=lambda: gear_calculation(dp.get()),
                     bg='#f7e6d0')
gear_button.grid(row=4, column=0)


#The Unit Calculator Frame
unit_frame = LabelFrame(master=root, text="Unit Convertor", bg='#7a6d17')
unit_frame.grid(row=1, column=1, padx=5, pady=5)

#Drop Down menu for the calculator frame
conversion_options = ['Time', 'Distance', 'Weight/Mass', 'Angle', 'Metric Prefixes']
#The type of conversion which will be decided by the user clicking
conversion_type = StringVar()
#But we will set it to first in list as default
conversion_type.set(conversion_options[0])
conversion_type_drop = OptionMenu(unit_frame, conversion_type, *conversion_options)
conversion_type_drop.pack()
unit_label = Label(unit_frame, text="UNITSSS", bg='#7a6d17', width=20, height=20)
unit_label.pack()

#Drop-down of unit to convert FROM

#Drop-down of unit to convert TO

#Entry widget

#button to press to make the conversion

#display result


#The Decimal/Fraction Convertor
decfrac_frame = LabelFrame(root, text="Decimal/Fraction Convertor", bg='#e09758')
decfrac_frame.grid(row=1, column=2, padx=5, pady=5)

#fraction to decimal
frac_to_dec_frame = LabelFrame(decfrac_frame, text="Fraction to Decimal", bg='#e09758')
frac_to_dec_frame.grid(row=0, column=0)
frac_dec_instruction = Label(frac_to_dec_frame, text="Please insert the fraction as numerator/denominator  Ex: 1/2",
                             padx=5, pady=5, bg='#e09758')
frac_dec_instruction.pack()
frac_dec_entry = Entry(frac_to_dec_frame, width=15)
frac_dec_entry.pack(pady=5)


def place_frac_to_dec():
    """
    find and pass numerator and denominator to functions in the frac_dec file to then insert into the result entry box
    :return: None
    """
    fraction = str(frac_dec_entry.get())
    if "/" in fraction:
        fraction_lst = fraction.split("/")
        numerator = int(fraction_lst[0])
        denominator = int(fraction_lst[1])
        decimal = frac_dec.frac_to_dec(numerator, denominator)
        frac_dec_result.delete(0, END)
        frac_dec_result.insert(END, decimal)


frac_dec_result_label = Label(frac_to_dec_frame, text="The decimal value of this fraction is: ", bg="#c79554")
frac_dec_result_label.pack(pady=5)
frac_dec_compute = Button(frac_to_dec_frame, text="Compute", bg="#c79554", command=place_frac_to_dec)
frac_dec_compute.pack(pady=5)
frac_dec_result = Entry(frac_to_dec_frame, width=10)
frac_dec_result.pack(pady=5)

dec_frac_instruction_text = "Insert any non-repeating parts of the number as a decimal in the box on the left\n " \
                            "(Ex: .1 or 0.1) and enter any repeating parts of the number "\
                            "in the box on the right \n(Ex: .1666 " \
                            "would have .1 on the left and .06 on the right."
#decimal to fraction
dec_to_frac_frame = LabelFrame(decfrac_frame, text="Decimal to Fraction", bg='#e09758')
dec_to_frac_frame.grid(row=1, column=0, pady=5)
dec_to_frac_instruction = Label(dec_to_frac_frame, text=dec_frac_instruction_text,
                                bg='#e09758')
dec_to_frac_instruction.grid(row=0, column=0, columnspan=3, pady=5)
df_static_label = Label(dec_to_frac_frame, text="Non-Repeating Decimal:")
df_static_label.grid(row=1, column=0)
df_static_entry = Entry(dec_to_frac_frame, width=10)
df_static_entry.grid(row=2, column=0, padx=5, pady=5)

df_repeat_label = Label(dec_to_frac_frame, text="Repeating Decimal:")
df_repeat_label.grid(row=1, column=1)
df_repeat_entry = Entry(dec_to_frac_frame, width=10)
df_repeat_entry.grid(row=2, column=1, padx=5, pady=5)


def place_dec_frac():
    """
    find fraction equivalent of the decimal and put it in the correct result box based on the functions in frac_dec file
    :return: None
    """
    jump = 0
    try:
        repeat_decimal = str(df_repeat_entry.get())
        for i in range(len(repeat_decimal)):
            if repeat_decimal[i] == ".":
                i += 1
                while repeat_decimal[i] == '0':
                    i += 1
                jump = len(repeat_decimal[i:])
                break
        repeat_decimal = float(repeat_decimal)
    except ValueError:
        repeat_decimal = 0
    try:
        static_decimal = float(df_static_entry.get())
    except ValueError:
        static_decimal = 0
    numerator, denominator = frac_dec.repeating_nums(repeat_decimal, static_decimal, jump)
    numerator, denominator = frac_dec.simplify(numerator, denominator)
    string_fraction = str(numerator) + "/" + str(denominator)
    df_result.delete(0, END)
    df_result.insert(END, string_fraction)


df_compute_Button = Button(dec_to_frac_frame, width=10, text="Compute", command=place_dec_frac)
df_compute_Button.grid(row=3, column=0, columnspan=2, pady=5)
df_result_label = Label(dec_to_frac_frame, text="The resulting fraction is: ", width=18)
df_result_label.grid(row=4, column=0, columnspan=2, pady=5)
df_result = Entry(dec_to_frac_frame, width=18)
df_result.grid(row=5, column=0, columnspan=2, padx=5, pady=5)






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
    table_to_show = rTable(option, table_frame, row_offset=1)


#picking the size (metric vs standard)
hardware_sys_frame = LabelFrame(hardware_ref_frame, text="System")
hardware_sys_frame.grid(column=0, row=0, pady=15)
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
hardware_type_frame.grid(column=1, row=0, pady=15)
#radio buttons to pick between nuts and machine screws
screws = Radiobutton(hardware_type_frame, text="Screws", variable=var_2, value="sc", command=hardware_select)
screws.pack(side=LEFT)
#set this as the default
screws.invoke()
nuts = Radiobutton(hardware_type_frame, text='Nuts', variable=var_2, value="n", command=hardware_select)
nuts.pack(side=LEFT)

#hardware works cited
works_cited_frame = LabelFrame(hardware_ref_frame, text="My References")
works_cited_frame.grid(row=10, column=0, columnspan=3, pady=5)
works_cited_button = Button(works_cited_frame, text="Click for Works Cited", command=lambda:
                            works_cited(works_cited_frame), width=30, bg="#a89a6a")
works_cited_button.pack()

root.mainloop()
