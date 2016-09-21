"""
Module Description:
    Button left frame containing a notebook of listviews containing subjects as items
Interface for other modules:
    - get_selected_item() -> Get subject that is clicked at the moment
    - return_item(item) -> Get back an item into the list
Interface to other modules:
    NONE
Callbacks:
    TBD
"""


from ttk import  Frame
import ttk as nttk
from tkinter import *
import json
from GUI.TopFrames.TopRightFrame import *

selected_item = []
listbox_hauptpflicht = []
resource  =  []
treeview=()


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

        TopRightFrame.set_text(resource[1]['Description'], resource[1]['Content'] )

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
        global treeview
        treeview = nttk.Treeview(master=frame_hauptwahl, columns=['Semester', 'ECTS'])

        # First treeview column initialization
        treeview.heading('#0',text='Subject Name', anchor='w')
        treeview.heading('Semester', text="Semester", anchor='w')
        treeview.heading('ECTS', text='Credits', anchor='w')

        treeview.column('#0', width=300)
        treeview.column('Semester', width=50)
        treeview.column('ECTS', width=50)
        counter=0
        for item in resource:
            semester_string=item['Semester']
            if 'ss' in item['Semester'] or 'SS' in item['Semester']:
               semester_string='Sommer'
            elif 'WS'  in item['Semester'] or 'ws' in item['Semester']:
                semester_string='Winter'
            else:
                semester_string='Unknown'

            parent_id=treeview.insert('',counter,iid=counter,text=item['Name'], values=[semester_string, item['Credits']])
           # treeview.insert(parent_id, 0 , text="Description that might be too long to be shown I guess after I have read the documentation on the website from an american university")
            counter=counter+1
        treeview.pack(fill=BOTH,expand=TRUE)
        treeview.bind("<ButtonRelease-1>", self.button_clicked)

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

    #-------------------------- INTERFACES -------------------------------#
    @staticmethod
    def on_subject_changed(id_1, id_2):
        print("On subject changed was called!")
        print("Id1: " + str(id_1))
        print("Id2: " + str(id_2))

    def button_clicked(self, event):
        global treeview
        global resource
        self.update()
        item=treeview.focus()
        TopRightFrame.set_text(resource[int(item)]['Description'], resource[int(item)]['Content'])
