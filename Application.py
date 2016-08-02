from tkinter import *

class Application:
    def __init__(self, master):
        self.master=master
        frame = Frame(master)
        frame.pack()

        self.button_quit=Button(frame,text="Quit this shit", command=quit, width=100, state="disabled")
        self.button_quit.pack()

        self.button_toggle=Button(frame, text="Toggle the left button", command = dummy_callback())
        self.button_toggle.pack()
        self.button_toggle.bind("<Button-1>", dummy_callback())
"""
def toggle_button_state(button):
    print("Button has been pressed!")
    state = button.configure()
    if state["state"] == "disabled":
        button.configure(state="enabled")
    else:
        button.configure(state="disabled")
"""
def dummy_callback(event):
    print("Callback has been run!")
    button=event.widget
    button.configure(state="disabled")



