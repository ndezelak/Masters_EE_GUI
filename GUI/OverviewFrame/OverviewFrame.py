from ttk import  *
from tkinter import *



class OverviewFrame(Frame):
    def populateFrame(self):
        # Title for the overview section
        title_overview = Label(self, text="Overview")
        title_overview.pack(anchor=N, expand=TRUE)
