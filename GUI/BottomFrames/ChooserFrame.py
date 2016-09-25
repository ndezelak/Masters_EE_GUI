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

from ttk import Frame
import ttk as nttk
from tkinter import *
import json
from GUI.TopFrames.TopRightFrame import *
from GUI.TopFrames.TopLeftFrame import *

selected_item = [-1,-1]
listbox_hauptpflicht = []
resource = []
treeview_hauptwahl = ()
treeview_haupt=()
treeview_neben=()
categories=("ENERGY","MECHATRONIK", "NANO", "COMMUNICATION", "ELECTRONICS")
class_reference = []

class ChooserFrame(Frame):
    # Constructor, initializes the GUI elements
    def __init__(self, root):
        # Here you call the Frame constructor first and then place widgets into that frame
        super().__init__(root)
        self.populateFrame()
        class_reference=self
    #---------------- CLASS INNER METHODS --------------------------------------#
    def populateFrame(self):
        # Initial parsing of the .json file
        global resource
        if not resource:
            with open("Resources/rawfile.json", 'r') as file:
                resource = json.load(file)
            for item in resource:
                print(item['Name'])

        # ----------------------------------------------------------------------------------#
        # Subframe for "Haupt"
        frame_hauptpflicht = nttk.Frame()
        global treeview_haupt
        treeview_haupt=nttk.Treeview(master=frame_hauptpflicht, columns=['Semester', 'ECTS'])

        #Headings of the table
        treeview_haupt.heading('#0', text='Subject Name', anchor='w')
        treeview_haupt.heading('Semester', text="Semester", anchor='w')
        treeview_haupt.heading('ECTS', text='Credits', anchor='w')

        # Width settings
        treeview_haupt.column('#0', width=300)
        treeview_haupt.column('Semester', width=50)
        treeview_haupt.column('ECTS', width=50)

        treeview_haupt.pack(fill=BOTH,expand=TRUE)
        treeview_haupt.bind('<ButtonRelease-1>', lambda event,arg=1:  self.item_clicked(event, arg))
        #----------------------------------------------------------------------------------#
        # Subframe for "Hauptwahl"
        frame_hauptwahl = nttk.Frame()
        global treeview_hauptwahl
        treeview_hauptwahl = nttk.Treeview(master=frame_hauptwahl, columns=['Semester', 'ECTS'])

        treeview_hauptwahl.heading('#0', text='Subject Name', anchor='w')
        treeview_hauptwahl.heading('Semester', text="Semester", anchor='w')
        treeview_hauptwahl.heading('ECTS', text='Credits', anchor='w')

        treeview_hauptwahl.column('#0', width=300)
        treeview_hauptwahl.column('Semester', width=50)
        treeview_hauptwahl.column('ECTS', width=50)

        treeview_hauptwahl.pack(fill=BOTH, expand=TRUE)
        treeview_hauptwahl.bind("<ButtonRelease-1>",lambda event,arg=2:  self.item_clicked(event, arg))
        # ----------------------------------------------------------------------------------#
        # Subframe for "Nebenwahl"
        frame_nebenwahl = nttk.Frame()
        global treeview_neben
        treeview_neben = nttk.Treeview(frame_nebenwahl, columns=['Semester', 'ECTS'])

        treeview_neben.heading('#0', text='Subject Name', anchor='w')
        treeview_neben.heading('Semester', text="Semester", anchor='w')
        treeview_neben.heading('ECTS', text='Credits', anchor='w')

        treeview_neben.column('#0', width=300)
        treeview_neben.column('Semester', width=50)
        treeview_neben.column('ECTS', width=50)

        treeview_neben.pack(fill=BOTH, expand=TRUE)
        treeview_neben.bind('<ButtonRelease-1>', lambda event,arg=3:  self.item_clicked(event, arg))
        #----------------------------------------------------------------------------------------#
        # Notebook construction (using frame objects)
        notebook = nttk.Notebook(self)
        notebook.add(frame_hauptpflicht, text="Wahlpflicht")
        notebook.add(frame_hauptwahl, text="Wahl")
        notebook.add(frame_nebenwahl, text="Nebenwahl")
        notebook.pack(side=LEFT, fill=BOTH, expand=TRUE)
        notebook.pack_propagate(0)

    # -------------------------------------------------------#
    # Method returning a list of subjects (type:dict) that belong to the category
    @staticmethod
    def filter_subjects(category):
        subject_2_return=[]
        global resource
        counter=0
        for subject in resource:
            if 'Categories' in subject and 'Type' in subject:
                # Hack to distinguish between an obligatory and a free subject
                fault_category=category+'!'

                if category[-1:] is "!":
                    type="Wahlpflicht"
                elif category[-1:] is "*":
                    type="Nebenwahl"
                    fault_category=category[:-1] + "!"
                else:
                    type="Wahl"
                    # First statement makes sure a "wahl" subject does not get through if a "subject!" is the category
                    # Seconds statement allows a subject that is either wahlpflicht and from the category (without ! at the end)
                    # or directly from the category with a " at the end
                    # Third statement lets through everything if type is nebenwahl
                if (type is "Wahl" and subject['Type'] == 'Wahl\n' and category in subject['Categories'] and fault_category not in subject['Categories'] )\
                or (type is "Wahlpflicht" and ((subject['Type'] == 'Wahlpflicht\n' and category[:-1] in subject['Categories'])
                                                       or category in subject['Categories']))\
                or type is "Nebenwahl" and (category[:-1] in subject['Categories'] or fault_category in subject['Categories']):
                    subject['Index'] = counter
                    subject_2_return.append(subject)
            counter = counter + 1
        return subject_2_return

    # -------------------------- INTERFACES -------------------------------#
    @staticmethod
    # Method that is called by other modules to refresh chooser frame with new data
    def on_subject_changed(id_1, id_2):
        global selected_item
        global resource
        global treeview_hauptwahl

        # ------------- Helper function ---------------#
        def add_items_to_list(treeview, category):
            counter = 0
            subjects_done = []
            treeview.delete(*treeview.get_children())
            for subject in ChooserFrame.filter_subjects(category):
                if subject['Name'] not in subjects_done:
                    semester_string = subject['Semester']
                    # Modification of the semester string for better readibility
                    if 'ss' in semester_string or 'SS' in semester_string:
                        semester_string = 'Sommer'
                    elif 'WS' in semester_string or 'ws' in semester_string:
                        semester_string = 'Winter'
                    else:
                        semester_string = 'Unknown'
                    # Add subject to the treeview
                    treeview.insert(parent='', index=subject['Index'], iid=subject['Index'],
                                    text=subject['Name'], values=[semester_string, subject['Credits']])

                    # Save which subjects have been already added in the current session
                    subjects_done.append(subject['Name'])
                counter = counter + 1
        # -------------------------------------------------------#
        # Check which subject category has changed
        if selected_item[0] != id_1 and id_1 !=0:
            item=id_1
            selected_item[0]=id_1

        elif selected_item[1] != id_2 and id_2 !=0:
            item=id_2
            selected_item[1] = id_2
        else:
            return

        if item == id_1:
            add_items_to_list(treeview_hauptwahl, categories[item-1])
            add_items_to_list(treeview_haupt, categories[item-1]+"!")

        else:
            add_items_to_list(treeview_neben, categories[item-1]+"*")

    # -------------------------------------------------------#
    def getSelectedItem(self):
        global listbox_hauptpflicht
        index = listbox_hauptpflicht.curselection()
        # Return 0 if no item is currently selected
        if (index):
            return listbox_hauptpflicht.get(index, last=index)[0]
        else:
            return 0

    # -------------------------- CALLBACKS---------------------------------#
    def item_clicked(self, event, arg):
        global treeview_hauptwahl
        global treeview_haupt
        global treeview_neben
        global resource

        # Method focus() returns the item iid that is currently focused
        if arg == 1:
            item = treeview_haupt.focus()
        elif arg ==2:
            item = treeview_hauptwahl.focus()
        elif arg==3:
            item = treeview_neben.focus()
        else:
            item=0

        print("Item iid is:" + item)
        if "I0" in item:
            item=0
        if item =="":
            return
        TopRightFrame.set_text(resource[int(item)]['Description'], resource[int(item)]['Content'])
