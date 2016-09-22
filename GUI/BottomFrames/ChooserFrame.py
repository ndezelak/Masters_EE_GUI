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

class ChooserFrame(Frame):
    # Constructor, initializes the GUI elements
    def __init__(self, root):
        # Here you call the Frame constructor first and then place widgets into that frame
        super().__init__(root)
        self.populateFrame()

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

        # Ask LeftTopFrame which subject is currently selected
        self.update_idletasks()
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

        treeview_haupt.pack(fill=BOTH,expand=TRUE)
        treeview_haupt.bind('<ButtonRelease-1>', self.item_clicked)
        '''
        counter = 0
        for item in resource:
            semester_string = item['Semester']
            if 'ss' in item['Semester'] or 'SS' in item['Semester']:
                semester_string = 'Sommer'
            elif 'WS' in item['Semester'] or 'ws' in item['Semester']:
                semester_string = 'Winter'
            else:
                semester_string = 'Unknown'

            parent_id = treeview_hauptwahl.insert('', counter, iid=counter, text=item['Name'],
                                                  values=[semester_string, item['Credits']])
            # treeview.insert(parent_id, 0 , text="Description that might be too long to be shown I guess after I have read the documentation on the website from an american university")
            counter = counter + 1
        '''
        treeview_hauptwahl.pack(fill=BOTH, expand=TRUE)
        treeview_hauptwahl.bind("<ButtonRelease-1>", self.item_clicked)
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
        treeview_neben.bind('<ButtonRelease-1>', self.item_clicked)
        #----------------------------------------------------------------------------------------#
        # Notebook construction (using frame objects)
        notebook = nttk.Notebook(self)
        notebook.add(frame_hauptpflicht, text="Wahlpflicht")
        notebook.add(frame_hauptwahl, text="Wahl")
        notebook.add(frame_nebenwahl, text="Nebenwahl")
        notebook.pack(side=LEFT, fill=BOTH, expand=TRUE)


    # -------------------------- INTERFACES -------------------------------#
    @staticmethod
    def on_subject_changed(id_1, id_2):
        global selected_item
        global resource
        global treeview_hauptwahl
        if selected_item[0]==-1:
            selected_item[0]=id_1
            selected_item[1]=id_2
        if selected_item[0] != id_1:
            item=id_1
            selected_item[0]=id_1
        elif selected_item[1] != id_2:
            item=id_2
            selected_item[1] = id_2
        else:
            return

        if item == id_1:
            # Delete all subjects as new will come
            treeview_hauptwahl.delete(*treeview_hauptwahl.get_children())
            print("You will make hauptwahl to " + categories[item-1])
            counter=0
            subjects_done=[]
            for subject in resource:
                category=[]
                if subject['Categories']:
                    category = subject['Categories']
                if categories[item-1] in category :
                    if not subject['Name'] in subjects_done:
                        semester_string = subject['Semester']
                        if 'ss' in semester_string or 'SS' in semester_string:
                            semester_string = 'Sommer'
                        elif 'WS' in semester_string or 'ws' in semester_string:
                            semester_string = 'Winter'
                        else:
                            semester_string = 'Unknown'
                        treeview_hauptwahl.insert(parent='',index=counter,
                                          text=subject['Name'], values=[semester_string, subject['Credits'] ])
                        counter=counter+1
                        subjects_done.append(subject['Name'])
        else:
            print("You will make nebenwahl to " + categories[item-1])




    def getSelectedItem(self):
        global listbox_hauptpflicht
        index = listbox_hauptpflicht.curselection()
        # Return 0 if no item is currently selected
        if (index):
            return listbox_hauptpflicht.get(index, last=index)[0]
        else:
            return 0

    # -------------------------- CALLBACKS---------------------------------#
    def item_clicked(self, event):
        global treeview_hauptwahl
        global resource

        # Method focus() returns the item iid that is currently focused
        item = treeview_hauptwahl.focus()
        TopRightFrame.set_text(resource[int(item)]['Description'], resource[int(item)]['Content'])
