from tkinter import *
import units


#This class handles the UI for the unit convertor
class UnitsUI:
    def __init__(self, master_frame):
        """
        By creating objects of this class, the UI for the unit convertor is created and inserted into the specified
        frame
        :param master_frame: the label frame where the UI should be inserted in to
        """
        self.master = master_frame
        # Radio Buttons for unit type
        type_frame = LabelFrame(self.master, text="Conversion Type", bg='#ada168')
        type_frame.grid(row=0, column=0, padx=5, pady=5)
        self.conversion_type = StringVar()
        time_radio = Radiobutton(type_frame, text="Time", variable=self.conversion_type, value='Time',
                                 command=self.unit_conversion_type,
                                 bg="#ada168")
        time_radio.grid(row=0, column=0, sticky="w")
        dist_radio = Radiobutton(type_frame, text="Distance", variable=self.conversion_type, value="Distance",
                                 command=self.unit_conversion_type, bg="#ada168")
        dist_radio.grid(row=1, column=0, sticky="w")
        wm_radio = Radiobutton(type_frame, text="Weight/Mass", variable=self.conversion_type, value="Weight/Mass",
                               command=self.unit_conversion_type, bg="#ada168")
        wm_radio.grid(row=2, column=0, sticky="w")
        angle_radio = Radiobutton(type_frame, text="Angle", variable=self.conversion_type, value="Angle",
                                  command=self.unit_conversion_type, bg="#ada168")
        angle_radio.grid(row=3, column=0, sticky="w")
        metric_radio = Radiobutton(type_frame, text="Metric Prefixes", variable=self.conversion_type,
                                   value="Metric Prefixes",
                                   command=self.unit_conversion_type, bg="#ada168")
        metric_radio.grid(row=4, column=0, sticky="w")

        # Value to convert items
        self.convert_frame = LabelFrame(self.master, text="Unit to Convert")
        self.convert_frame.grid(row=1, column=0, pady=5, padx=5)
        convert_value_instruction = Label(self.convert_frame, text="Value to be Converted:", padx=5, pady=2)
        convert_value_instruction.grid(row=0, column=0)
        self.convert_value_entry = Entry(self.convert_frame, width=10)
        self.convert_value_entry.grid(row=1, column=0)
        # Unit to convert from
        convert_unit_instruction = Label(self.convert_frame, text="Original Unit:", padx=5, pady=2)
        convert_unit_instruction.grid(row=2, column=0)
        self.orig_unit = StringVar()
        # default set it to time (next 2 lines)
        self.unit_options = units.time_units
        self.orig_unit.set(self.unit_options[0])
        convert_units = OptionMenu(self.convert_frame, self.orig_unit, *self.unit_options)
        convert_units.grid(row=3, column=0)

        # Unit to convert TO
        self.convert_result_frame = LabelFrame(self.master, text="Equivalent Measure:")
        self.convert_result_frame.grid(row=2, column=0, padx=5, pady=5)
        convert_result_unit_instruction = Label(self.convert_result_frame, text="Resulting Unit:")
        convert_result_unit_instruction.grid(row=0, column=0)
        self.result_unit = StringVar()
        # set it to time as default to match the input
        result_unit_list = units.time_units
        self.result_unit.set(result_unit_list[0])
        result_unit_menu = OptionMenu(self.convert_result_frame, self.result_unit, *result_unit_list)
        result_unit_menu.grid(row=1, column=0)

        convert_result_instruction = Label(self.convert_result_frame, text="The equivalent unit is ", padx=5, pady=2)
        convert_result_instruction.grid(row=2, column=0)
        self.convert_result = Entry(self.convert_result_frame, width=10)
        self.convert_result.grid(row=3, column=0)

        # now that the initial and resulting unit frames have been created, turn the time radio button on by default
        time_radio.invoke()
        # button to press to make the conversion
        compute_unit_button = Button(self.master, text="Compute", command=self.compute_units)
        compute_unit_button.grid(column=0, row=3, pady=4)

    def unit_conversion_type(self):
        """
        gets the conversion type from radio buttons and subsequently changes the drop-down
        options for the actual unit selection (both convert from and to)
        :return: None
        """
        con_type = str(self.conversion_type.get())
        updated_unit_options = units.get_unit_list(con_type)

        # update the initial unit
        self.orig_unit.set(updated_unit_options[0])
        convert_units = OptionMenu(self.convert_frame, self.orig_unit, *updated_unit_options)
        convert_units.grid(row=3, column=0)

        # Update the result unit
        self.result_unit.set(updated_unit_options[0])
        result_unit_menu = OptionMenu(self.convert_result_frame, self.result_unit, *updated_unit_options)
        result_unit_menu.grid(row=1, column=0)

    def compute_units(self):
        """
        Function for hitting the compute button and calculating the unit conversion. Logic is located in the 'units'
        module. This function uses those functions to display it in the UI
        :return:
        """
        initial_unit = str(self.orig_unit.get())
        end_unit = str(self.result_unit.get())
        type_to_convert = str(self.conversion_type.get())
        conversion_value = float(self.convert_value_entry.get())
        print(initial_unit, end_unit, type_to_convert, conversion_value)
        result_value = units.conversion(type_to_convert, initial_unit, end_unit, conversion_value)
        self.convert_result.delete(0, END)
        self.convert_result.insert(0, result_value)
