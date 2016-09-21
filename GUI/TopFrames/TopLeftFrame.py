
"""
Module Description:
    Top left frame containing radio buttons that enable the user to choose its study direction
Interface for other modules:
    - get_selected_subjects()
Interface to other modules:
    [ChooserFrame]- on_subject_changed(id_1,id_2)
Callbacks:
    - radiobutton_clicked(button_id)
"""

from tkinter import *
from ttk import *
from GUI.BottomFrames.ChooserFrame import ChooserFrame

# Has to be here in order to be global
# No call of IntVar() on this stage is allowed!
haupt_option = () # Variable used for the main subject radiobutton group
neben_option = () # Variable used for the other subject radiobutton group
option_buffer = [1, 1]  # Used for storing the last valid radibutton group value
rbuttons_left = [] # Radiobuttons lying in the left column
rbuttons_right = [] # Radiobuttons lying in the right column


class TopLeftFrame(Frame):
    'This class represents the top left frame content of the GUI'
    frame = ()
    number = 0
    root = ()

    # Constructor, initializes the GUI elements
    def __init__(self, root):
        # Here you call the Frame constructor first and then place widgets into that frame
        super().__init__(root)
        self.populateFrame()

    def populateFrame(self):
        # Defines teo labels representing your main and your second choice for study
        # Defines radio buttons representing different options

        label_hauptwahl = Label(self, text="Hauptwahl")
        label_hauptwahl.grid(column=0, row=0)

        label_nebenwahl = Label(self, text="Nebenwahl")
        label_nebenwahl.grid(column=1, row=0)

        # List of strings representing main study areas
        texts = ["Energietechnik", "Mechatronik", "Nanotechnology", "Kommunikationstechnik", "Computers & Electronics"]
        # Pack those strings into Label widgets
        option_labels = []
        for i in range(0, 5):
            option_labels.append(Label(self, text=texts[i]))
            option_labels[i].grid(column=2, row=2 + i, sticky=W)

        # Radiobutton initialization
        global haupt_option
        global neben_option
        global rbuttons_left
        global rbuttons_right

        neben_option = IntVar()
        haupt_option = IntVar()

        # Create a list of RadioButton objects
        for i in range(0, 5):

            rbuttons_left.append(
                Radiobutton(self, variable=haupt_option, value=i + 1, command=lambda :self.radiobutton_clicked(0))   )
            rbuttons_right.append(
                Radiobutton(self, variable=neben_option, value=i + 1, command=lambda: self.radiobutton_clicked(1))   )
            # Set default radio button position
            if i == 2:
                rbuttons_left[i].invoke()
                global option_buffer
                option_buffer[0] = 2
            if i == 1:
                rbuttons_right[i].invoke()
                global option_buffer
                option_buffer[1] = 1

            # Place buttons into the right grid row and column
            rbuttons_left[i].grid(column=0, row=2 + i)
            rbuttons_right[i].grid(column=1, row=2 + i)

        # Configure the main frame
        self.columnconfigure(0, weight=2)
        self.columnconfigure(1, weight=2)
        self.columnconfigure(2, weight=6)


    # -------- RADIOBUTTON CALLBACK FUNCTION ---------#
    def radiobutton_clicked(self,rbutton_id):
        # global haupt_option
        global haupt_option
        global neben_option

        print("---------------------------------")
        # Radiobutton from group "main subject"
        if rbutton_id == 0:
            print("position value radiobutton 1 changed to " + str(haupt_option.get()))
            # Check if the user wants to make a mistake
            if haupt_option.get() == neben_option.get():
                global rbuttons_left
                global option_buffer
                index = option_buffer[0]-1
                print("Values are the same! Calculated radio button index is:" + str(index))
                rbuttons_left[index].invoke()
                return
            # Update the ChooserFrame about a setting change
            if option_buffer[0] != haupt_option.get():
                print("Calling ob_subject_changed")
                ChooserFrame.on_subject_changed(haupt_option.get(), neben_option.get())
                option_buffer[0] = haupt_option.get()
        else:
            print("position value radiobutton 2 changed  to " + str(neben_option.get()))
            if haupt_option.get() == neben_option.get():
                global rbuttons_right
                global option_buffer
                index = option_buffer[1]-1
                print("Values are the same! Calculated radi button index is:" + str(index))
                rbuttons_right[index].invoke()
                return
            # Update the ChooserFrame about a setting change
            if option_buffer[1] != neben_option.get():
                print("Calling ob_subject_changed")
                ChooserFrame.on_subject_changed(haupt_option.get(), neben_option.get())
                option_buffer[1] = neben_option.get()


    # ------------INTERFACES-------------#
    # Interface to other modules so that they can read the current radiobutton state
    @staticmethod
    def get_selected_subjects():
        package=[]
        package.append(haupt_option.get())
        package.append(neben_option.get())
        return package
