from ttk import  Frame
import ttk as nttk
from tkinter import *
class ChooserFrame(Frame):


    def populateFrame(self):
        # Subframe for "Hauptwahlpflicht"
        txt = nttk.Label(text="Item")
        frame_hauptpflicht = nttk.Frame()
        listbox_hauptpflicht = Listbox(frame_hauptpflicht)
        listbox_hauptpflicht.insert(0,'Item1')
        listbox_hauptpflicht.insert(1, 'Item1')
        listbox_hauptpflicht.insert(2, 'Item1')
        listbox_hauptpflicht.pack(expand=TRUE, fill=BOTH)

        # Subframe for "Hauptwahl"
        frame_hauptwahl = nttk.Frame()
        txt = nttk.Label(frame_hauptwahl, text="Some text")
        txt.pack(side=LEFT, expand=TRUE, fill=BOTH)
        button_sample = nttk.Button(frame_hauptwahl, text="Click me!")
        button_sample.pack(side=LEFT, expand=TRUE, fill=BOTH)

        # Notebook construction (using frame objects)
        notebook = nttk.Notebook(self)
        notebook.add(frame_hauptpflicht, text="Hauptwahlpflicht")
        notebook.add(frame_hauptwahl, text="Hauptwahl")
        notebook.pack(side=LEFT, fill=BOTH, expand=TRUE)