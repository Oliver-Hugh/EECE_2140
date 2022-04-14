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

#entry for num teeth in gear 1
gear_1_frame = LabelFrame(gear_frame, text="Gear 1 # of Teeth:", bg='#c98a00')
gear_1_frame.grid(column=0, row=1, pady=10, padx=4)
gear_1_entry = Entry(gear_1_frame, width=15, bg='#f7e6d0')
gear_1_entry.pack()
#entry for num teeth in gear 2
gear_2_frame = LabelFrame(gear_frame, text="Gear 2 # of Teeth:", bg='#c98a00')
gear_2_frame.grid(column=0, row=2, pady=10, padx=4)
gear_2_entry = Entry(gear_2_frame, width=15, bg='#f7e6d0')
gear_2_entry.pack()
#Drop-down for dp
dp_frame = LabelFrame(gear_frame, text="Diametral Pitch", bg='#f7e6d0')
dp_frame.grid(column=0, row=3, pady=20, padx=10)
#list of standard diametral pitches
dp_list = [12, 16, 18, 20, 24, 32, 48]
dp = IntVar()
dp_drop = OptionMenu(dp_frame, dp, *dp_list)
dp_drop.pack(pady=2)
dp.set(dp_list[0])
#include a blank label to increase the size of the frame
spacer_label = Label(dp_frame, text="", width=15, bg='#f7e6d0')
spacer_label.pack()
gear_result_frame = LabelFrame(gear_frame, text="Center to Center distance:", bg='#f7e6d0')
gear_result_frame.grid(row=5, column=0, pady=20)
gear_result = Entry(gear_result_frame, width=15, bg='#f7e6d0')
gear_result.pack(pady=8)


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
gear_button.grid(row=4, column=0, pady=10)


#The Unit Calculator Frame
unit_frame = LabelFrame(master=root, text="Unit Convertor", bg='#7a6d17')
unit_frame.grid(row=1, column=1, padx=5, pady=5)

#Radio Buttons for unit type
type_frame = LabelFrame(unit_frame, text="Conversion Type", bg='#ada168')
type_frame.grid(row=0, column=0, padx=5, pady=5)
conversion_type = StringVar()


def unit_conversion_type():
    """
    gets the conversion type from radio buttons and subsequently changes the drop-down
    options for the actual unit selection (both convert from and to)
    :return: None
    """
    con_type = str(conversion_type.get())
    updated_unit_options = units.get_unit_list(con_type)

    #update the initial unit
    orig_unit.set(updated_unit_options[0])
    convert_units = OptionMenu(convert_frame, orig_unit, *updated_unit_options)
    convert_units.grid(row=3, column=0)

    #Update the result unit
    result_unit.set(updated_unit_options[0])
    result_unit_menu = OptionMenu(convert_result_frame, result_unit, *updated_unit_options)
    result_unit_menu.grid(row=1, column=0)


time_radio = Radiobutton(type_frame, text="Time", variable=conversion_type, value='Time', command=unit_conversion_type,
                         bg="#ada168")
time_radio.grid(row=0, column=0, sticky="w")
dist_radio = Radiobutton(type_frame, text="Distance", variable=conversion_type, value="Distance",
                         command=unit_conversion_type, bg="#ada168")
dist_radio.grid(row=1, column=0, sticky="w")
wm_radio = Radiobutton(type_frame, text="Weight/Mass", variable=conversion_type, value="Weight/Mass",
                       command=unit_conversion_type, bg="#ada168")
wm_radio.grid(row=2, column=0, sticky="w")
angle_radio = Radiobutton(type_frame, text="Angle", variable=conversion_type, value="Angle",
                          command=unit_conversion_type, bg="#ada168")
angle_radio.grid(row=3, column=0, sticky="w")
metric_radio = Radiobutton(type_frame, text="Metric Prefixes", variable=conversion_type, value="Metric Prefixes",
                           command=unit_conversion_type, bg="#ada168")
metric_radio.grid(row=4, column=0, sticky="w")

# Value to convert items
convert_frame = LabelFrame(unit_frame, text="Unit to Convert")
convert_frame.grid(row=1, column=0, pady=5, padx=5)
convert_value_instruction = Label(convert_frame, text="Value to be Converted:", padx=5, pady=2)
convert_value_instruction.grid(row=0, column=0)
convert_value_entry = Entry(convert_frame, width=10)
convert_value_entry.grid(row=1, column=0)
#Unit to convert from
convert_unit_instruction = Label(convert_frame, text="Original Unit:", padx=5, pady=2)
convert_unit_instruction.grid(row=2, column=0)
orig_unit = StringVar()
#default set it to time (next 2 lines)
unit_options = units.time_units
orig_unit.set(unit_options[0])
convert_units = OptionMenu(convert_frame, orig_unit, *unit_options)
convert_units.grid(row=3, column=0)

#Unit to convert TO
convert_result_frame = LabelFrame(unit_frame, text="Equivalent Measure:")
convert_result_frame.grid(row=2, column=0, padx=5, pady=5)
convert_result_unit_instruction = Label(convert_result_frame, text="Resulting Unit:")
convert_result_unit_instruction.grid(row=0, column=0)
result_unit = StringVar()
#set it to time as default to match the input
result_unit_list = units.time_units
result_unit.set(result_unit_list[0])
result_unit_menu = OptionMenu(convert_result_frame, result_unit, *result_unit_list)
result_unit_menu.grid(row=1, column=0)

convert_result_instruction = Label(convert_result_frame, text="The equivalent unit is ", padx=5, pady=2)
convert_result_instruction.grid(row=2, column=0)
convert_result = Entry(convert_result_frame, width=10)
convert_result.grid(row=3, column=0)

#now that the initial and resulting unit frames have been created, turn the time radio button on by default
time_radio.invoke()


def compute_units():
    """
    Function for hitting the compute button and calculating the unit conversion. Logic is located in the 'units'
    module. This function uses those functions to display it in the UI
    :return:
    """
    initial_unit = str(orig_unit.get())
    end_unit = str(result_unit.get())
    type_to_convert = str(conversion_type.get())
    conversion_value = float(convert_value_entry.get())
    print(initial_unit, end_unit, type_to_convert, conversion_value)
    result_value = units.conversion(type_to_convert, initial_unit, end_unit, conversion_value)
    convert_result.delete(0, END)
    convert_result.insert(0, result_value)


#button to press to make the conversion
compute_unit_button = Button(unit_frame, text="Compute", command=compute_units)
compute_unit_button.grid(column=0, row=3, pady=4)


#The Decimal/Fraction Convertor
decfrac_frame = LabelFrame(root, text="Decimal/Fraction Convertor", bg='#e09758')
decfrac_frame.grid(row=1, column=2, padx=5, pady=4)

#fraction to decimal
frac_to_dec_frame = LabelFrame(decfrac_frame, text="Fraction to Decimal", bg='#e09758')
frac_to_dec_frame.grid(row=0, column=0)
frac_dec_instruction = Label(frac_to_dec_frame, text="Please insert the fraction as numerator/denominator  Ex: 1/2",
                             padx=5, pady=5, bg='#e09758')
frac_dec_instruction.pack(padx=10)
frac_dec_entry = Entry(frac_to_dec_frame, width=15)
frac_dec_entry.pack(pady=4)


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
frac_dec_result_label.pack(pady=4)
frac_dec_compute = Button(frac_to_dec_frame, text="Compute", bg="#c79554", command=place_frac_to_dec)
frac_dec_compute.pack(pady=4)
frac_dec_result = Entry(frac_to_dec_frame, width=10)
frac_dec_result.pack(pady=4)

dec_frac_instruction_text = "Insert any non-repeating parts of the number as a decimal\n in the LEFT box " \
                            "and enter any repeating parts "\
                            "in the RIGHT\n box (Ex: .1666 " \
                            "would have .1 on the left and .06 on the right)."
#decimal to fraction
dec_to_frac_frame = LabelFrame(decfrac_frame, text="Decimal to Fraction", bg='#e09758')
dec_to_frac_frame.grid(row=1, column=0, pady=4)
dec_to_frac_instruction = Label(dec_to_frac_frame, text=dec_frac_instruction_text,
                                bg='#e09758', padx=5)
dec_to_frac_instruction.grid(row=0, column=0, columnspan=3, pady=4)
df_static_label = Label(dec_to_frac_frame, text="Non-Repeating Decimal:")
df_static_label.grid(row=1, column=0)
df_static_entry = Entry(dec_to_frac_frame, width=10)
df_static_entry.grid(row=2, column=0, padx=5, pady=4)

df_repeat_label = Label(dec_to_frac_frame, text="Repeating Decimal:")
df_repeat_label.grid(row=1, column=1)
df_repeat_entry = Entry(dec_to_frac_frame, width=10)
df_repeat_entry.grid(row=2, column=1, padx=5, pady=4)


def place_dec_frac():
    """
    find fraction equivalent of the decimal and put it in the correct result box based on the functions in frac_dec file
    :return: None
    """
    jump = 0
    try:
        repeat_decimal = float(df_repeat_entry.get())
    except ValueError:
        repeat_decimal = 0
    try:
        static_decimal = float(df_static_entry.get())
    except ValueError:
        static_decimal = 0
    numerator, denominator = frac_dec.repeating_nums(repeat_decimal, static_decimal)
    numerator, denominator = frac_dec.simplify(int(numerator), int(denominator))
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
