
from tkinter import *
from ttk import *
class TopLeftFrame(Frame):
    'This class represents the top left frame content of the GUI'
    frame=()
    number=0


    def populateFrame(self):
        #Defines teo labels representing your main and your second choice for study
        #Defines radio buttons representing different options
        label_hauptwahl = Label(self, text="Hauptwahl")
        label_hauptwahl.grid(column=0, row=0 )

        label_nebenwahl = Label(self, text="Nebenwahl")
        label_nebenwahl.grid(column=1, row=0)

        texts=["Energietechnik","Mechatronik","Nanotechnology","Kommunikationstechnik","Computers & Electronics"]
        option_labels=[]
        for i in range(0,5):
            option_labels.append(Label(self,text=texts[i]) )
            option_labels[i].grid(column=2, row=2+i, sticky=W)

        # Radiobutton initialization
        rbuttons_left=[]
        rbuttons_right = []
        haupt_option=1
        neben_option=0
        for i in range(0,5):
            rbuttons_left.append(Radiobutton(self,variable=haupt_option, value=i+1) )
            rbuttons_right.append(Radiobutton(self, variable=neben_option, value=i+5))
            if i == 2:
                rbuttons_left[i].invoke()
            if i == 1:
                rbuttons_right[i].invoke()
            rbuttons_left[i].grid(column=0, row = 2+i)
            rbuttons_right[i].grid(column=1, row=2 + i)

        self.columnconfigure(0,weight=2)
        self.columnconfigure(1, weight=2)
        self.columnconfigure(2, weight=6)


