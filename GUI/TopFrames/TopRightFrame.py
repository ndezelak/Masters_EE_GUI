from ttk import  Frame,Label
from tkinter import *


text_widget = ()
text_to_display=()
content_to_display=()
class TopRightFrame(Frame):

    def __init__(self, root):
        super().__init__(root)
        self.populateFrame()


    def populateFrame(self):
        global text_widget
        global text_to_display
        global content_to_display
        content_to_display=StringVar()
        text_to_display=StringVar()
        text_to_display.set("Some text")

        label_frame_description=LabelFrame(self,labelanchor=NW, text="Description")
        #label_frame_description.pack_propagate(0)

        text_widget = Message(label_frame_description, aspect=300, textvariable=text_to_display,
                              justify=LEFT, width=500)
        text_widget.pack(anchor=N, fill=BOTH, expand=TRUE)
        label_frame_description.pack(anchor=N, fill=BOTH, expand=TRUE)

        label_frame_content = LabelFrame(self, labelanchor=NW, text="Content")
        #label_frame_content.pack_propagate(0)
        text_widget_2 = Message(label_frame_content, aspect=300, textvariable=content_to_display,
                              justify=LEFT, width=500)
        text_widget_2.pack(anchor=N, fill=BOTH, expand=TRUE)
        label_frame_content.pack(anchor=N, fill=BOTH, expand=TRUE)



    @staticmethod
    def set_text(text_as_string, content):
        global text_to_display
        global content_to_display
        text_to_display.set(text_as_string)
        content_to_display.set(content)



