from tkinter import *

class Application:
    def __init__(self, master):
        self.master=master
        frame = Frame(master)
        frame.pack()

        button_quit=Button(frame,text="Quit this shit", command=quit)
        button_quit.pack()
        button_quit.bind()





