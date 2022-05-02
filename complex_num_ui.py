from tkinter import *
from complex_nums import ComplexExpression


#This class is responsible for the UI associated with the complex number calculator
class ComplexNumUI:

    def __init__(self, master_frame):
        """
        Create ComplexNumUI objects which will create the UI in the master_frame: the LabelFrame where this calculator
        will go
        :param master_frame: a LabelFrame where the complex num ui should show up in the main file
        """
        self.master = master_frame
        #frame for instructions and input
        input_frame = LabelFrame(self.master, text="Input and Instructions", bg="#eb6b34")
        input_frame.grid(row=0, column=0, padx=10, pady=5)
        instruction_label = Label(input_frame, text="Enter a complex number or equation that involves complex numbers "
                                                    "below. Use i or j for the imaginary component.\n Use the button "
                                                    "below to input numbers in polar form. Please put the coefficient "
                                                    "of the imaginary component at the beginning or\nend of the term. "
                                                    "If the imaginary component is just -j or -i, please make it -1j or"
                                                    " -1i. Please put an operator before parenthesis.", bg="#eb6b34")
        instruction_label.pack(side=TOP)
        self.input_entry = Entry(input_frame, width=50)
        self.input_entry.pack(side=TOP)

        angle_button = Button(input_frame, width=10, text=u"\u2220", command=self.angle_press, bg="#eb6b34")
        angle_button.pack(side=TOP)

        answer_label_frame = LabelFrame(self.master, text="Result", bg="#eb6b34")
        answer_label_frame.grid(row=0, column=1, padx=10, pady=5)
        self.var_1 = StringVar()
        polar_radio = Radiobutton(answer_label_frame, text="Polar", variable=self.var_1, value="po",
                                  command=self.form_select, bg="#eb6b34")
        polar_radio.grid(row=0, column=0)
        #set on as default
        polar_radio.invoke()
        rect_radio = Radiobutton(answer_label_frame, text="Rectangular", variable=self.var_1, value="r",
                                 command=self.form_select, bg="#eb6b34")
        rect_radio.grid(row=0, column=1)

        self.result_entry = Entry(answer_label_frame, width=30)
        self.result_entry.grid(row=1, column=0, columnspan=2, padx=5, pady=5)
        compute_button = Button(answer_label_frame, text="Compute", width=7, command=self.compute)
        compute_button.grid(row=2, column=0, columnspan=2, pady=2)

    def form_select(self):
        """
        Getting the form that the answer should be displayed in from the radio buttons - either "po" for polar
        or "r" for rectangular
        :return: the answer form (either polar or rectangular) as a string
        """
        answer_form = str(self.var_1.get())
        return answer_form

    def compute(self):
        """
        computing the answer by creating a ComplexExpression object, and inserting the answer in the result entry box
        :return: None
        """
        self.result_entry.delete(0, END)
        string_exp = self.input_entry.get()
        print(self.form_select())
        answer = ComplexExpression(string_exp, self.form_select()).answer
        self.result_entry.insert(END, answer)

    def angle_press(self):
        """
        This method inputs the angle symbol inside the input entry box
        :return: None
        """
        self.input_entry.insert(END, u"\u2220")
