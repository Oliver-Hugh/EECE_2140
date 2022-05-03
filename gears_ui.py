from tkinter import *
import gears


#This class handles the UI for the gear calculator
class GearCalculator:

    def __init__(self, master_frame):
        """
        By creating an object of this class, the UI for the gear calculator is created and inserted in the specified
        frame
        :param master_frame: The label frame where UI for this feature should be inserted
        """
        self.master_frame = master_frame
        #entry for num teeth in gear 1
        gear_1_frame = LabelFrame(self.master_frame, text="Gear 1 # of Teeth:", bg='#c98a00')
        gear_1_frame.grid(column=0, row=1, pady=10, padx=4)
        self.gear_1_entry = Entry(gear_1_frame, width=15, bg='#f7e6d0')
        self.gear_1_entry.pack()
        #entry for num teeth in gear 2
        gear_2_frame = LabelFrame(self.master_frame, text="Gear 2 # of Teeth:", bg='#c98a00')
        gear_2_frame.grid(column=0, row=2, pady=10, padx=4)
        self.gear_2_entry = Entry(gear_2_frame, width=15, bg='#f7e6d0')
        self.gear_2_entry.pack()
        #Drop-down for dp
        dp_frame = LabelFrame(self.master_frame, text="Diametral Pitch", bg='#f7e6d0')
        dp_frame.grid(column=0, row=3, pady=20, padx=10)
        #list of standard diametral pitches
        dp_list = ["12", "16", "18", "20", "24", "32", "48"]
        dp = IntVar()
        dp_drop = OptionMenu(dp_frame, dp, *dp_list)
        dp_drop.pack(pady=2)
        dp.set(dp_list[0])
        #include a blank label to increase the size of the frame
        spacer_label = Label(dp_frame, text="", width=15, bg='#f7e6d0')
        spacer_label.pack()
        gear_result_frame = LabelFrame(master_frame, text="Center to Center distance:", bg='#f7e6d0')
        gear_result_frame.grid(row=5, column=0, pady=20)
        self.gear_result = Entry(gear_result_frame, width=15, bg='#f7e6d0')
        self.gear_result.pack(pady=8)
        gear_dp = dp.get()
        self.create_button(gear_dp)

    def gear_calculation(self, gear_dp):
        """
        This function calculates the center to center distance of 2 gears using functions from the
        gears file and inserts the result inside the gear_result entry
        :param gear_dp: the diametral pitch of the gears
        :return: None
        """
        teeth_1 = int(self.gear_1_entry.get())
        teeth_2 = int(self.gear_2_entry.get())

        if type(teeth_1) is int and type(teeth_2) is int and teeth_1 is not None and teeth_2 is not None:
            #now use functions from the gears file to calculate the center to center distance
            gear_answer = gears.calculate_center(teeth_1, teeth_2, gear_dp)
            self.gear_result.delete(0, END)
            self.gear_result.insert(END, str(gear_answer) + " in")

    def create_button(self, gear_dp):
        """
        This method creates the button that is pressed to calculate the center to center distance of 2 gears
        :param gear_dp: the gear dp as a string
        :return: None
        """
        # button to calculate. This is created after the entry (even though it is above it) because its command
        # function references the gear_result entry
        gear_button = Button(self.master_frame, width=15, text="Calculate Result",
                             command=lambda: self.gear_calculation(gear_dp), bg='#f7e6d0')
        gear_button.grid(row=4, column=0, pady=10)
