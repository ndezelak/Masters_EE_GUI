from ttk import  *
from tkinter import *
#import main_GUI as main

semester_text = ['WS 2017', 'SS  2017', 'WS 2018', 'SS  2018', 'WS 2019', 'SS  2019']
semester_boxes = []
semester_frames = []

class OverviewFrame(Toplevel):
    def __init__(self):
        self.visible=1
        super().__init__()
    @staticmethod
    def add_item(id, subject):
        global semester_boxes
        for box in semester_boxes:
            if box.id == id:
                if ( ("ss" or "SS") in subject['Semester'] and ("SS" or "ss") in id) or ("WS" in subject['Semester'] and "WS" in id):
                    box.insert(END, subject['Name'])
                    return 1
        return 0

    def save_data(self):
        #from main_GUI import frame_overview
        #frame_overview=None
        self.visible=0
        self.destroy()

    def populateFrame(self):
        # Basic window settings
        self.title("Overview Window")
        self.minsize(width=600, height=600)

        #Overwrite close window function
        self.protocol('WM_DELETE_WINDOW', lambda: self.save_data())

        # Main window frame
        topWindow_frame = Frame(self)
        topWindow_frame.pack(side=TOP, expand=TRUE, fill=BOTH)

        # Canvas inside the main frame
        mcanvas = Canvas(topWindow_frame, width=300, scrollregion=(0, 0, 100, 1100))
        # Frame inside the canvas
        frame_overview = Frame(mcanvas)
        # Vertical scrollbar attached to the main frame. What is scrolled is the canvas
        mscrollbar = Scrollbar(topWindow_frame, orient=VERTICAL, command=mcanvas.yview)
        # Combine scrolling with the canvas
        mcanvas.configure(yscrollcommand=mscrollbar.set)

        # Packing of the widgets
        mscrollbar.pack(fill=Y, side=RIGHT)
        mcanvas.pack(side=LEFT, fill=BOTH)
        # Attach the other frame to the canvas
        mcanvas.create_window((0, 0), window=frame_overview, anchor='nw')

        # Load image TODO: Not working yet!
        imagepath = 'GUI\\OverviewFrame\\kos.gif'
        mimage = PhotoImage(file=imagepath)
        image_ = mimage.subsample(5, 5)

        # Define semesters as Listboxes inside Labelframes
        for i in range(1, 7):
            list_frame = LabelFrame(frame_overview, text=semester_text[i - 1])
            listbox = Listbox(list_frame, height=10, width=50)

            listbox.id = semester_text[i - 1]
            listbox.pack(side=LEFT, anchor=NW)
            list_frame.pack(side=TOP, anchor=NW)
            list_frame.id = semester_text[i - 1]

            # Save references to widgets globally to use in other functions
            global semester_boxes,semester_frames
            semester_boxes.append(listbox)
            semester_frames.append(list_frame)

        # Right frame used for displaying statistic information
        frame_statistik = LabelFrame(topWindow_frame, text="Statistik", font=('Times', '13'))
        label_test = Label(frame_statistik, image=image_)
        label_test.pack()
        credits_label = Label(frame_statistik, text="DELETE", relief=RAISED, font=('Times', '16') , height=3, width=20)
        credits_label.pack(side=BOTTOM, anchor=S)
        frame_statistik.pack(side=LEFT, anchor=NW, expand=TRUE, fill=BOTH)

