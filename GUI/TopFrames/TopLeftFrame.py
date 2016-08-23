from ttk import Frame,Label
class TopLeftFrame(Frame):
    'This class represents the top left frame content of the GUI'
    frame=()
    number=0


    def populateFrame(self):
        label = Label(self, text="Top Left Frame")
        label.pack()

