from ttk import  Frame
import ttk as nttk
from tkinter import *
import json

selected_item = []
listbox_hauptpflicht = []
resource  =  []



class ChooserFrame(Frame):

    # Constructor, initializes the GUI elements
    def __init__(self, root):
        # Here you call the Frame constructor first and then place widgets into that frame
        super().__init__(root)
        self.populateFrame()

    def populateFrame(self):

        global resource
        with open("Resources/rawfile.json", 'r') as file:
            resource = json.load(file)


        global selected_item
        selected_item = StringVar()

        # Subframe for "Hauptwahlpflicht"
        txt = nttk.Label(text="Item")
        frame_hauptpflicht = nttk.Frame()
        global listbox_hauptpflicht
        listbox_hauptpflicht = Listbox(frame_hauptpflicht, activestyle = 'dotbox', listvariable = selected_item)
        counter=0
        for subject in resource:
            listbox_hauptpflicht.insert(counter, subject['Name'])
            counter = counter + 1


        listbox_hauptpflicht.pack(expand=TRUE, fill=BOTH)

        # Subframe for "Hauptwahl"
        frame_hauptwahl = nttk.Frame()
        txt = nttk.Label(frame_hauptwahl, text="Some text")
        txt.pack(side=LEFT, expand=TRUE, fill=BOTH)
        button_sample = nttk.Button(frame_hauptwahl, text="Click me!")
        button_sample.pack(side=LEFT, expand=TRUE, fill=BOTH)

         #Notebook construction (using frame objects)
        notebook = nttk.Notebook(self)
        notebook.add(frame_hauptpflicht, text="Hauptwahlpflicht")
        notebook.add(frame_hauptwahl, text="Hauptwahl")
        notebook.pack(side=LEFT, fill=BOTH, expand=TRUE)

        # Used as an interface for other widgets to get the content of the currently selected line
    def getSelectedItem(self):
        global listbox_hauptpflicht
        index = listbox_hauptpflicht.curselection()
        # Return 0 if no item is currently selected
        if (index):
            return listbox_hauptpflicht.get(index, last=index)[0]

        else:
            return 0
    @staticmethod
    def on_subject_changed(id_1, id_2):
        print("On subject changed was called!")
        print("Id1: " + str(id_1))
        print("Id2: " + str(id_2))
