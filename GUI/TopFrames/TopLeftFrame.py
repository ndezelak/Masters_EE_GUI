
from tkinter import *
from ttk import *




# Has to be here in order to be global
# No call of IntVar() on this stage is allowed!
haupt_option = ()
neben_option = ()

class TopLeftFrame(Frame):
    'This class represents the top left frame content of the GUI'
    frame=()
    number=0
    root=()

    def setRoot(self,root):
        self.root=root


    def populateFrame(self):
        #Defines teo labels representing your main and your second choice for study
        #Defines radio buttons representing different options

        label_hauptwahl = Label(self, text="Hauptwahl")
        label_hauptwahl.grid(column=0, row=0 )

        label_nebenwahl = Label(self, text="Nebenwahl")
        label_nebenwahl.grid(column=1, row=0)

        # List of strings representing main study areas
        texts=["Energietechnik","Mechatronik","Nanotechnology","Kommunikationstechnik","Computers & Electronics"]
        # Pack those strings into Label widgets
        option_labels=[]
        for i in range(0,5):
            option_labels.append(Label(self,text=texts[i]) )
            option_labels[i].grid(column=2, row=2+i, sticky=W)

        # Radiobutton initialization
        global haupt_option
        haupt_option = IntVar()

        global neben_option
        neben_option = IntVar()

        rbuttons_left=[]
        rbuttons_right = []

        for i in range(0,5):

            rbuttons_left.append(Radiobutton(self,variable=haupt_option, value=i+1,command=main_subject_callback)    )
            rbuttons_right.append(Radiobutton(self, variable=neben_option, value=i+1, command=main_subject_callback))
            if i == 2:
                rbuttons_left[i].invoke()
            if i == 1:
                rbuttons_right[i].invoke()

            # Place buttons into the right grid row and column
            rbuttons_left[i].grid(column=0, row = 2+i)
            rbuttons_right[i].grid(column=1, row=2 + i)

        # Configure the main frame
        self.columnconfigure(0,weight=2)
        self.columnconfigure(1, weight=2)
        self.columnconfigure(2, weight=6)


def main_subject_callback():
    #global haupt_option
    global haupt_option
    global neben_option
    print("Callback called")
    print("position value radiobutton 1 is " + str(haupt_option.get()))
    print("position value radiobutton 2 is " + str(neben_option.get()))

