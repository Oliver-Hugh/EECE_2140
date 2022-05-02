from tkinter import *
import frac_dec


#This class handles the UI for the fraction/decimal convertor feature
class FracDecUI:

    def __init__(self, master_frame):
        """
        By creating objects of this class, the UI is created and inserted into the specified frame
        :param master_frame: the LabelFrame where the UI for this feature should be added
        """
        self.master = master_frame

        #fraction to decimal
        frac_to_dec_frame = LabelFrame(self.master, text="Fraction to Decimal", bg='#e09758')
        frac_to_dec_frame.grid(row=0, column=0)
        frac_dec_instruction = Label(frac_to_dec_frame, text="Please insert the fraction as numerator/denominator  "
                                                             "Ex: 1/2", padx=5, pady=5, bg='#e09758')
        frac_dec_instruction.pack(padx=10)
        self.frac_dec_entry = Entry(frac_to_dec_frame, width=15)
        self.frac_dec_entry.pack(pady=4)

        frac_dec_result_label = Label(frac_to_dec_frame, text="The decimal value of this fraction is: ", bg="#c79554")
        frac_dec_result_label.pack(pady=4)
        frac_dec_compute = Button(frac_to_dec_frame, text="Compute", bg="#c79554", command=self.place_frac_to_dec)
        frac_dec_compute.pack(pady=4)
        self.frac_dec_result = Entry(frac_to_dec_frame, width=10)
        self.frac_dec_result.pack(pady=4)

        dec_frac_instruction_text = "Insert any non-repeating parts of the number as a decimal\n in the LEFT box " \
                                    "and enter any repeating parts " \
                                    "in the RIGHT\n box (Ex: .1666 " \
                                    "would have .1 on the left and .06 on the right)."
        # decimal to fraction
        dec_to_frac_frame = LabelFrame(self.master, text="Decimal to Fraction", bg='#e09758')
        dec_to_frac_frame.grid(row=1, column=0, pady=4)
        dec_to_frac_instruction = Label(dec_to_frac_frame, text=dec_frac_instruction_text,
                                        bg='#e09758', padx=5)
        dec_to_frac_instruction.grid(row=0, column=0, columnspan=3, pady=4)
        df_static_label = Label(dec_to_frac_frame, text="Non-Repeating Decimal:")
        df_static_label.grid(row=1, column=0)
        self.df_static_entry = Entry(dec_to_frac_frame, width=10)
        self.df_static_entry.grid(row=2, column=0, padx=5, pady=4)

        df_repeat_label = Label(dec_to_frac_frame, text="Repeating Decimal:")
        df_repeat_label.grid(row=1, column=1)
        self.df_repeat_entry = Entry(dec_to_frac_frame, width=10)
        self.df_repeat_entry.grid(row=2, column=1, padx=5, pady=4)
        df_compute_button = Button(dec_to_frac_frame, width=10, text="Compute", command=self.place_dec_frac)
        df_compute_button.grid(row=3, column=0, columnspan=2, pady=5)
        df_result_label = Label(dec_to_frac_frame, text="The resulting fraction is: ", width=18)
        df_result_label.grid(row=4, column=0, columnspan=2, pady=5)
        self.df_result = Entry(dec_to_frac_frame, width=18)
        self.df_result.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

    def place_frac_to_dec(self):
        """
        find & pass numerator and denominator to functions in the frac_dec file to then insert into the result entry box
        :return: None
        """
        fraction = str(self.frac_dec_entry.get())
        if "/" in fraction:
            fraction_lst = fraction.split("/")
            numerator = int(fraction_lst[0])
            denominator = int(fraction_lst[1])
            decimal = frac_dec.frac_to_dec(numerator, denominator)
            self.frac_dec_result.delete(0, END)
            self.frac_dec_result.insert(END, decimal)

    def place_dec_frac(self):
        """
        find fraction equivalent of the decimal and put it in the correct result box based on the
        functions in frac_dec file
        :return: None
        """
        try:
            repeat_decimal = float(self.df_repeat_entry.get())
        except ValueError:
            repeat_decimal = 0
        try:
            static_decimal = float(self.df_static_entry.get())
        except ValueError:
            static_decimal = 0
        numerator, denominator = frac_dec.repeating_nums(repeat_decimal, static_decimal)
        numerator, denominator = frac_dec.simplify(int(numerator), int(denominator))
        string_fraction = str(numerator) + "/" + str(denominator)
        self.df_result.delete(0, END)
        self.df_result.insert(END, string_fraction)
