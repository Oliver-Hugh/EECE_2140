# Oliver Hugh 4/4/2022
from tkinter import *


class Table:

    metric_screws = [
        ["Screw", "Close Fit (mm)", "Standard Fit (mm)"],
        ["M2", "2.10", "2.20"],
        ["M3", "3.15", "3.30"],
        ["M4", "4.20", "4.40"],
        ["M5", "5.25", "5.50"],
        ["M6", "6.30", "6.60"],
        ["M7", "7.40", "7.70"],
        ["M8", "8.40", "8.80"]]
    standard_screws = [
        ["Screw", "Close Fit (in)", "Free Fit (in)"],
        ["#2", ".0890", ".0960"],
        ["#3", ".1040", ".1100"],
        ["#4", ".1160", ".1285"],
        ["#6", ".1440", ".1495"],
        ["#8", ".1695", ".1770"],
        ["#10", ".1960", ".2010"],
        ["1/4", ".2570", ".2660"]]
    metric_nuts = [
        ["Screw", "Diameter (mm)", "Height (mm)"],
        ["M2", "4", "1.5"],
        ["M3", "5.5", "2.4"],
        ["M4", "7", "3.2"],
        ["M5", "8", "4"],
        ["M6", "10", "5"],
        ["M7", "11", "5.5"],
        ["M8", "13", "6.6"]]
    standard_nuts = [
        ["Screw", "Diameter (in)", "Height (in)"],
        ["#2", "3/16", "1/16"],
        ["#3", "3/16", "1/16"],
        ["#4", "1/4", "3/32"],
        ["#6", "5/16", "7/64"],
        ["#8", "11/32", "1/8"],
        ["#10", "3/8", "1/8"],
        ["1/4", "7/16", "3/16"]]

    def __init__(self, data: int, area, row_offset: int):
        """
        Initiates a Table object, which will create a table in tkinter
        to display data
        :param data: the data that will be displayed in the table. Should be a number 1-4:
            1: metric screws, 2: standard screws 3: metric nuts 4: standard nuts
        :param area: where the table will be packed
        :param row_offset: how many other items are above the table. This is needed so that the table can be
        properly shifted down so that the grid system will work out
        """
        self.data = data
        self.area = area
        #the data lines up for all 4 different possible data sets, so we are arbitrarily measuring the lengths of this
        #one, as it will work for all
        num_rows = len(self.standard_screws)
        num_col = len(self.standard_screws[0])

        if data == 1:
            data = self.metric_screws
        elif data == 2:
            data = self.standard_screws
        elif data == 3:
            data = self.metric_nuts
        elif data == 4:
            data = self.standard_nuts
        else:
            raise ValueError("Data parameter in Table must be an integer between 1 and 4")

        #we will now iterate through the elements in data
        #to create a matrix of entries, which we will then display data in
        #go through rows
        for r in range(num_rows):
            for c in range(num_col):
                self.box = Entry(master=self.area, width=12, bg="#ada168")
                self.box.grid(row=r+row_offset, column=c)
                self.box.insert(END, data[r][c])


def works_cited(area: str):
    worked_cited_window = Toplevel(area)
    worked_cited_window.title("Works Cited")
    cite_1 = """[1]    Bolt Depot. "Metric Nut Sizes", boltdepot.com
    https://www.boltdepot.com/fastener-information/nuts-washers/Metric-Nut-Dimensions.aspx (accessed April 12, 2022)"""
    cite_2 = """[2]    Bolt Depot. "US Nut Size Table", boltdepot.com. 
    https://www.boltdepot.com/fastener-information/nuts-washers/us-nut-dimensions.aspx (accessed April 12, 2022)"""
    cite_3 = """[3]     LittleMachineShop. "Metric Screw Size", littlemachineshop.com. 
    https://littlemachineshop.com/images/gallery/PDF/tapdrillsizes.pdf (accessed April 11, 2022)."""
    cite_4 = """[4]     LittleMachineShop. "Tap and Clearance Drill Sizes", littlemachineshop.com. 
    https://littlemachineshop.com/reference/tapdrill.php (accessed April 11, 2022). """

    citation_1 = Label(master=worked_cited_window, text=cite_1)
    citation_1.grid(row=0, column=0)
    citation_2 = Label(master=worked_cited_window, text=cite_2)
    citation_2.grid(row=1, column=0)
    citation_3 = Label(master=worked_cited_window, text=cite_3)
    citation_3.grid(row=2, column=0)
    citation_4 = Label(master=worked_cited_window, text=cite_4)
    citation_4.grid(row=3, column=0)
